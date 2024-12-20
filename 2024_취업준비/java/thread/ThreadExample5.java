public class ThreadExample5 {
    public static final void main(String[] args) throws InterruptedException {
        Runnable task = () -> {
            try {
                while (true) {
                    System.out.println("hello, Lambda Runnable!");
                    Thread.sleep(100);
                }
            } catch (InterruptedException ie) {
                System.out.println("I'm interrupter");
            }
        };

        Thread thread = new Thread(task);
        thread.start();
        Thread.sleep(500);
        thread.interrupt();
        System.out.println("Hello, My Interrupted Child");
    }
} 