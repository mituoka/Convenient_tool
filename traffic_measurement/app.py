import psutil
from sklearn.metrics import r2_score
r2_score(y_true, y_pred)

def main():
    # メモリ容量を取得
    mem = psutil.virtual_memory() 
    print(mem.total)
    
    print range(3)
    # メモリ使用量を取得 
    print(mem.used)

    # メモリ空き容量を取得 
    print(mem.available)

    # CPU使用率を取得 
    cpu = psutil.cpu_percent(interval=1)
    print(cpu)

# プログラム7｜mainを呼び出す
if __name__ == "__main__":
    main()