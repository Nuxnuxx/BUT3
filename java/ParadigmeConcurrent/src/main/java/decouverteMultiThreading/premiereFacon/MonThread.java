package decouverteMultiThreading.premiereFacon;

import java.util.concurrent.TimeUnit;

public class MonThread extends Thread {
    private String message;
    private boolean termine;

    public MonThread(String message) {
        this.message = message;
    }

    public void run() {
        termine = true;
        while (termine) {
            System.out.println(message +"------"+ Thread.currentThread().getName());
        }
    }

    public void mettreFin(){
        this.termine = false;
    }
}
