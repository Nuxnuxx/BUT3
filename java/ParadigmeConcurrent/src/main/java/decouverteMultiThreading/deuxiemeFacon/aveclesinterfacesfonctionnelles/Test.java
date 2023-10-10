package decouverteMultiThreading.deuxiemeFacon.aveclesinterfacesfonctionnelles;

import java.util.concurrent.TimeUnit;

public class Test {

    public static void main(String[] args) {
        Runnable premierRunabble;

        premierRunabble=()->{
            for (int i = 0; i < 45; i++) {
                System.out.println("premierRunnable - "+ i);

                try {
                    TimeUnit.MILLISECONDS.sleep(400);
                } catch (InterruptedException e) {

                }
            }
        };

        Thread t1 = new Thread(premierRunabble);

        t1.start();

        new Thread(()->{{
            for (int i = 0; i < 45; i++) {
                System.out.println("premierRunnable - "+ i);

                try {
                    TimeUnit.MILLISECONDS.sleep(400);
                } catch (InterruptedException e) {

                }
            }
        }}
        ).start();
    }
}
