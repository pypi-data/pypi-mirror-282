from libcpp.string cimport string

cdef extern from "iarduino_I2C_PI.cpp":
    pass

cdef extern from "iarduino_I2C_Joystick.cpp":
    pass

cdef extern from "iarduino_I2C_Joystick.h":
    cdef cppclass iarduino_I2C_Joystick:
        iarduino_I2C_Joystick() except +
        iarduino_I2C_Joystick(unsigned char) except +
        bint begin()
        bint changeAddress(unsigned char)
        bint reset()
        unsigned char getAddress()
        unsigned char getVersion()
        bint getPullI2C()
        bint setPullI2C(bint)
        unsigned short getButton(unsigned char)
        int getPosition_X()
        int getPosition_Y()
        int getADC_X()
        int getADC_Y()
        bint setCalibration_X(int, int, int)
        bint setCalibration_Y(int, int, int)
        bint setDeadZone(float)
        bint setAveraging(unsigned char)
        bint updateCalX()
        bint updateCalY()
        int getMinX()
        int getCenX()
        int getMaxX()
        int getMinY()
        int getCenY()
        int getMaxY()
        void changeBus(string)
