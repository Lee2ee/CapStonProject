# -라인 트레이서 주행
# 데이터 수집
from pop import Pilot

cam = Pilot.Camera(width=300, height=300)
cam.show()

dataCollector = Pilot.Data_Collector(Pilot.Track_Follow, camera=cam)

# 데이터 딥러닝
LF = Pilot.Track_Follow(camera=cam)
LF.load_datasets()

LF.train(times=5)

value = LF.run()
print(value)

LF.show()

Car = Pilot.AutoCar()
Car.setSpeed(50)


def drive(value):
    Car.forward()
    steer = value['x']

    if steer > 1:
        steer = 1
    elif steer < -1:
        steer = -1

    Car.steering = steer * 1.5


while True:
    LF.run(callback=drive)

# - 목표물 추적
# 학습 모델 활용

from pop import Pilot

cam = Pilot.Camera(width=300, height=300)
ac = Pilot.AutoCar()
OF = Pilot.Object_Follow(cam)
OF.load_model()

v = OF.detect(index='person')
print(v)

v = OF.detect(index='person')
print(v)

OF.show()

while True:
    v = OF.detect(index='person')

    if v is not None:
        steer = v['x'] * 4

        if steer > 1:
            steer = 1
        elif steer < -1:
            steer = -1

        ac.steering = steer

        if v['size_rate'] < 0.20:
            ac.forward(50)
        else:
            ac.stop()
    else:
        ac.stop()