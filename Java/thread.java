class MyRunnable implements Runnable {
    private String threadName;
    private int ncycle;
    public MyRunnable(String name) {
        this.threadName = name;
    }

    public void setncycle (int n){
        ncycle=n;
    }
    @Override
    public void run() {
        for (int i = 0; i < ncycle; i++) {
            
        }
    }
}

public class thread {
    int a;
    public static void main(String[] args) {
        Thread thread1 = new Thread(new MyRunnable("线程1"));
        Thread thread2 = new Thread(new MyRunnable("线程2"));
        
        thread1.start(); // 启动线程1
        thread2.start(); // 启动线程2
        
        try {
            thread1.join(); // 等待线程1结束
            thread2.join(); // 等待线程2结束
        } catch (InterruptedException e) {
            System.out.println("主线程被中断!");
        }
        
        System.out.println("所有线程已完成!");
    }
}

