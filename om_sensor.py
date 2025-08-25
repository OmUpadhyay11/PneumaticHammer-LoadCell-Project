import time
import u6

def main():
    d = u6.U6()
    d.getCalibrationData()
    
    try:
        while True:
            ain0 = d.getAIN(0)
            ain1 = d.getAIN(1)

            print(f"I: {ain0:.4f} V | V: {ain1:.4f} V")
            time.sleep(0.5)
            
    except KeyboardInterrupt:
        print("Exiting...") 
    finally:
        d.close()   
        
if __name__ == "__main__":
    main()