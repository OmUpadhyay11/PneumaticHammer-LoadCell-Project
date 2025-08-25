import u6, time

d = u6.U6()
d.getCalibrationData()

print("Driver OK. Reading AIN0/AIN1 once per 0.5s. Ctrl+C to stop.")
try:
    while True:
        v0 = d.getAIN(0)   # current output or unused
        v1 = d.getAIN(1)   # your A1A Vout if wired to AIN1
        print(f"AIN0={v0:.4f} V | AIN1={v1:.4f} V")
        time.sleep(0.5)
except KeyboardInterrupt:
    print("\nStopping…")
finally:
    d.close()
