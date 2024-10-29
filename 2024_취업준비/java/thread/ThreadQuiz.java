class Runner implements Runnable {
    public void run() {
        for (int i = 0; i <3; i++)
            System.out.printf("A ");
    }
}


public class ThreadQuiz {
    public static final void main(String[] args) throws Exception {
        Thread thread = new Thread(new Runner());
        System.out.printf("B ");
        thread.start();
        System.out.printf("C ");
        // runnable thread 작업 완료 까지 대기
        thread.join();
        System.out.printf("D ");
    }
    
}
