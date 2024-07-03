from ctypes import (
    c_byte,
    c_int,
    c_uint,
    byref,
    Array,
    CDLL,
    c_uint16,
    c_float,
    c_uint8,
)
from time import perf_counter_ns
from typing import Self, Literal, Any, Callable, Tuple, TypeAlias

from .constant import LIB_FILE_PATH, BinaryIO
from .loader import load_lib
from .logger import _logger

E6 = 1000000

"""
Only For IO, mode and level
OUTPUT = 1
INPUT = 0
HIGH = 1
LOW = 0
"""
# this will create a function that returns a C array, but it can't be recognized correctly by the pycharm
ADCArrayType: Callable = c_uint16 * 10  # type: ignore
# on 32bit machine, this will create a C array of 3 floats with bit-width of 4 bytes
MPUArrayType: Callable = c_float * 3  # type: ignore

ADCDataPack: TypeAlias = Tuple[int, int, int, int, int, int, int, int, int, int]
MPUDataPack: TypeAlias = Tuple[float, float, float]

__TECHSTAR_LIB__: CDLL = load_lib(LIB_FILE_PATH)


# 定义_WORD为无符号短整型
_WORD = c_uint16


class OnBoardSensors:
    """
    provides sealed methods accessing to the IOs and builtin sensors

    Owns 10 ADC channels and 3 MPU channels  and 8 IO channels

    ADC: 9 for normal use, 1 for power voltage measurement(the last element in the seq)
    IO: all the 8 are for normal use
    MPU: all the 3 are for normal use
    """

    def __init__(self, adc_min_sample_interval_ms: int = 5):
        """
        Initializes an instance of the OnBoardSensors class.
        init the ADC, IO and MPU data slots
        init sample freq limiter

        *Will NOT init the IO, ADC and MPU , you need to do it manually


        Parameters:
            adc_min_sample_interval_ms (int): The minimum sample interval in milliseconds for the ADC channels. Defaults to 5.

        Examples:
            >>> on_board = OnBoardSensors().adc_io_open().set_all_io_mode(0).set_all_io_levels(1).MPU6500_Open()
        """

        self._adc_cache: ADCDataPack = (0,) * 10
        self._adc_all: Array = ADCArrayType()
        self._accel_all: Array = MPUArrayType()
        self._gyro_all: Array = MPUArrayType()
        self._atti_all: Array = MPUArrayType()

        self.__adc_last_sample_timestamp: int = perf_counter_ns()

        self.__adc_min_sample_interval_ns: int = adc_min_sample_interval_ms * E6

    @property
    def last_sample_timestamp_ms(self) -> int:
        return int(self.__adc_last_sample_timestamp / E6)

    @property
    def adc_min_sample_interval_ms(self) -> int:
        """
        get the minimum interval between two consecutive samples, this is to prevent
        over-sampling, the value is in milliseconds。

        NOTE:
            the value is in milliseconds, but the unit is nanoseconds.
            a greater value means a lower rt performance
        """
        return int(self.__adc_min_sample_interval_ns / E6)

    @adc_min_sample_interval_ms.setter
    def adc_min_sample_interval_ms(self, value: int):
        self.__adc_min_sample_interval_ns = value * E6

    def adc_io_open(self) -> Self:
        """
        open the adc-io plug
        """
        _logger.info("Initializing ADC-IO")
        if (open_times := __TECHSTAR_LIB__.adc_io_open()) == -1:
            _logger.error("Failed to open ADC-IO")
        else:
            _logger.debug(f"ADC-IO open {open_times} times")
        return self

    def adc_io_close(self) -> Self:
        """
        close the adc-io plug
        """
        _logger.info("Closing ADC-IO")
        if __TECHSTAR_LIB__.adc_io_close() == -1:
            _logger.error("Failed to close ADC-IO")
            return
        _logger.debug("ADC-IO closed")
        return self

    def adc_all_channels(self) -> ADCDataPack:
        """
        Get all the ADC channels. Length = 10

        Returns:
            ADCDataPack: An array containing the values of all the ADC channels.
        """

        can_update_time = (
            self.__adc_last_sample_timestamp + self.__adc_min_sample_interval_ns
        )
        if can_update_time > (current := perf_counter_ns()):

            return self._adc_cache
        self.__adc_last_sample_timestamp = current
        if __TECHSTAR_LIB__.ADC_GetAll(self._adc_all):
            _logger.error("Failed to get all ADC channels")
        self._adc_cache = tuple(self._adc_all)
        return self._adc_cache  # type: ignore

    @staticmethod
    def io_all_channels() -> int:
        """
        get all io plug input levels

        uint8, each bit represents a channel, 1 for high, 0 for low

        Examples:
            0b10000000 => 第io7为高电平
            0b00000001 => 第io0为高电平
        """
        return __TECHSTAR_LIB__.adc_io_InputGetAll()

    @staticmethod
    def get_io_level(index: int) -> int:
        """
        Get the level of the specified IO index.

        Args:
            index (int): The index of the IO.

        Returns:
            int: The level of the specified IO index, which is calculated based on the result of adc_io_InputGetAll().

        Note:
            ONLY work in OUTPUT MODE
        """
        return (__TECHSTAR_LIB__.adc_io_InputGetAll() >> index) & 1

    def set_all_io_levels(self, levels: int) -> Self:
        """
        Sets the level of all IOs to the specified level.

        Args:
            levels (int): The level to set for all IOs.

        Returns:
            Self: The instance of the class.

        Raises:
            None
        Note:
            ONLY work in OUTPUT MODE
        Examples:
            levels = 0b0000 0001 => 第io0为高电平,其余为低电平
            levels = 0b1000 0000 => 第io7为高电平，其余为低电平
        """
        if __TECHSTAR_LIB__.adc_io_SetAll(c_uint(levels)):
            _logger.error("Failed to set all IO level")
        return self

    def flip_io_level(self, index: int) -> Self:
        """
        Flips the level of the specified IO index.
        Args:
            index:  The index of the IO.

        Returns:
            Self: The instance of the class.

        Notes:
            ONLY work in OUTPUT MODE
        """
        if __TECHSTAR_LIB__.adc_io_Set(c_uint(index)) == -1:
            _logger.error(f"Failed to flip IO level, index: {index}")
        return self

    @staticmethod
    def get_all_io_mode() -> int:
        """
        Get all IO modes. length = 8,store as bit0,bit1,bit2,bit3,bit4,bit5,bit6,bit7

        Returns:
            int: A buffer containing all IO modes.
        Examples:
            0b10000000 => 第io7为输出模式，可用于驱动舵机
            0b00000001 => 第io0为输入模式，可用于外接传感器
        """
        buffer = c_uint8()
        if __TECHSTAR_LIB__.adc_io_ModeGetAll(byref(buffer)) != 0:
            _logger.error("Failed to get all IO mode")
        return buffer.value

    def set_all_io_mode(self, mode: BinaryIO) -> Self:
        """
        Sets the mode of all IOs to the specified mode.

        Args:
            mode (Literal[0, 1]): The mode to set for all IOs. Must be either 0 or 1.

        Returns:
            Self: The instance of the class.

        Raises:
            None

        Description:
            This function sets the mode of all IOs to the specified mode using the `adc_io_ModeSetAll` method from the `TECHSTAR_LIB` library.
            If the `adc_io_ModeSetAll` method returns a truthy value, an error message is logged.
            The function returns the instance of the class.
        """
        mode_set = __TECHSTAR_LIB__.adc_io_ModeSet
        if any(mode_set(c_uint(index), c_int(mode)) for index in range(8)):
            _logger.error(f"Failed to set all IO mode to {mode}")
        return self

    def set_io_mode(
        self, index: Literal[0, 1, 2, 3, 4, 5, 6, 7] | int, mode: BinaryIO
    ) -> Self:
        """
        Sets the mode of the specified IO index to the specified mode.

        Args:
            index (Literal[0, 1]): The index of the IO. Must be either 0 or 1.
            mode (Literal[0, 1]): The mode to set for the IO. Must be either 0 or 1.

        Returns:
            Self: The instance of the class.

        Raises:
            None

        Description:
            This function sets the mode of the specified IO index to the specified mode using the `adc_io_ModeSet` method from the `TECHSTAR_LIB` library.
            If the `adc_io_ModeSet` method returns a truthy value, an error message is logged.
            The function returns the instance of the class.
        """
        if __TECHSTAR_LIB__.adc_io_ModeSet(c_uint(index), c_int(mode)):
            _logger.error(f"Failed to set IO mode, index: {index}, mode: {mode}")
        return self

    # <editor-fold desc="MPU section">
    def MPU6500_Open(self) -> Self:
        """
        initialize the 6-axis enhancer MPU6500
        default settings:
            acceleration: -+8G
            gyro: -+2000 degree/s
            sampling rate: 1kHz
        """
        _logger.info("Initializing MPU6500...")
        if __TECHSTAR_LIB__.mpu6500_dmp_init():
            _logger.warning("Failed to initialize MPU6500")
            return self
        _logger.info("MPU6500 initialized")
        return self

    def acc_all(self) -> MPUDataPack:
        """
        Retrieves the acceleration data from the MPU6500 sensor.

        Returns:
            MPUDataPack: An array containing the acceleration data.
        Notes:
            length = 3
            [0] ==> axis X
            [1] ==> axis Y
            [2] ==> axis Z
        """
        __TECHSTAR_LIB__.mpu6500_Get_Accel(
            self._accel_all
        )  # this function return a C pointer to the self._accel_all
        return tuple(self._accel_all)  # type: ignore

    def gyro_all(self) -> MPUDataPack:
        """
        Retrieves the gyroscope data from the MPU6500 sensor.

        Returns:
            MPUDataPack: An array containing the gyroscope data.

        Notes:
            length = 3
            [0] ==> axis X
            [1] ==> axis Y
            [2] ==> axis Z
        """

        __TECHSTAR_LIB__.mpu6500_Get_Gyro(
            self._gyro_all
        )  # this function return a C pointer to the self._gyro_all

        return tuple(self._gyro_all)  # type: ignore

    def atti_all(self) -> MPUDataPack:
        """
        Retrieves the attitude data from the MPU6500 sensor.

        Returns:
            MPUDataPack: An array containing the attitude data.

        Notes:
            length = 3
            [0] ==> Pitch|axis X
            [1] ==> Roll |axis Y
            [2] ==> Yaw  |axis Z
        """
        __TECHSTAR_LIB__.mpu6500_Get_Attitude(
            self._atti_all
        )  # this function return a C pointer to the self._atti_all

        return tuple(self._atti_all)  # type: ignore

    @staticmethod
    def get_handle(attr_name: str) -> Any:
        """
        Returns the attribute value of the TECHSTAR_LIB object corresponding to the given attribute name.
        Reserved to the user to harness other attributes of the TECHSTAR_LIB object.
        Args:
            attr_name (str): The name of the attribute to retrieve.

        Returns:
            Any: The value of the attribute.

        Raises:
            AttributeError: If the attribute does not exist in the TECHSTAR_LIB object.
        """
        return getattr(__TECHSTAR_LIB__, attr_name)

    @staticmethod
    def get_gyro_fsr() -> int:
        """
        Retrieves the Full Scale Range (FSR) of the gyroscope.

        This method queries and returns the FSR value of the gyroscope from the technology library.

        Returns:
            int: The Full Scale Range value of the gyroscope.
        """

        # Calls the technology library function to obtain the gyroscope's FSR, storing the result in fsr_value
        __TECHSTAR_LIB__.mpu_get_gyro_fsr(byref(fsr_value := _WORD()))
        return fsr_value.value

    @staticmethod
    def get_acc_fsr() -> int:
        """
        Retrieves the accelerometer full-scale range.

        This static method fetches the current full-scale range for the accelerometer from the TECHSTAR_LIB.

        Returns:
            int: The value representing the accelerometer full-scale range.
        """

        # Request the accelerometer full-scale range value
        __TECHSTAR_LIB__.mpu_get_accel_fsr(byref(fsr_value := c_byte()))
        # Return the obtained accelerometer full-scale range value
        return fsr_value.value

    def mpu_set_gyro_fsr(self, fsr: Literal[250, 500, 1000, 2000] | int) -> Self:
        """
        Sets the full-scale range for the gyroscope in the MPU.

        Parameters:
            fsr (Literal[250, 500, 1000, 2000] | int): Gyroscope full-scale range, can be one of 250, 500, 1000, or 2000 degrees per second.

        Returns:
            Self: Returns an instance of the function for method chaining.
        """

        # Call the underlying library function to set the gyroscope's full-scale range
        __TECHSTAR_LIB__.mpu_set_gyro_fsr(c_uint(fsr))
        return self

    def mpu_set_accel_fsr(self, fsr: Literal[2, 4, 8, 16] | int) -> Self:
        """
        Sets the accelerometer full-scale range (FSR) for the MPU.

        Parameters:
            fsr: Literal[2, 4, 8, 16] | int - The full-scale range of the accelerometer, with options being 2g, 4g, 8g, and 16g.

        Returns:
            Self: Returns the object itself to support method chaining.
        """

        __TECHSTAR_LIB__.mpu_set_accel_fsr(
            c_int(fsr)
        )  # Invokes the library function to set the accelerometer's FSR
        return self

    # </editor-fold>
