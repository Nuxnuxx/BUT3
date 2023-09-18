package decouverteMultiThreading.pabo;

import java.util.concurrent.TimeUnit;

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
            synchronized (System.out) {
                // String chaine = message +"------"+ Thread.currentThread().getName();
                String chaine = message;

                for (int c = 0; c < chaine.length(); c++) {
                    System.out.print(chaine.charAt(c));
                    try {
                        TimeUnit.MILLISECONDS.sleep(250);
                    } catch (InterruptedException e) {
                        throw new RuntimeException(e);
                    }
                    System.out.println();
                    // car on agit plus sur l'ecran (l'objet system out) apres cette ligne la
                }
            }
    }

    public void mettreFin() {
        this.termine = false;
    }
}
