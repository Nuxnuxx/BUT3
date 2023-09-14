package decouverteMultiThreading.deuxiemeFacon;

public class MonThread implements Runnable {
    private String message;
    private boolean termine;

    public MonThread(String message) {
        this.message = message;
    }

    @Override
    public void run() {
        termine = true;

        while (termine) {
            System.out.println(message +"------"+ Thread.currentThread().getName());
        }
    }

    public void mettreFin() {
        this.termine = false;
    }
}
