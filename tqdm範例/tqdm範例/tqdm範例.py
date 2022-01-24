from tqdm import tqdm,trange
import time
if __name__=="__main__":
    #進度條以9為單位
    for i in tqdm(range(9)):
        time.sleep(0.1)
    #for i in tqdm(range(100)):
    #    time.sleep(0.1)
   