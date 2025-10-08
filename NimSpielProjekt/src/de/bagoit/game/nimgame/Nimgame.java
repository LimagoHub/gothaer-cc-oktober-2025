package de.bagoit.game.nimgame;

import de.bagoit.game.Game;

import java.util.Scanner;

public class Nimgame implements Game{

    private final Scanner scanner = new Scanner(System.in);
    private int steine;

    public Nimgame() {
        steine = 23;
    }

    @Override
    public void play() {
        while(! isGameOver()) {
            playRound();
        }
    }

    private void playRound() {
        spielerzug();
        computerzug();
    }

    private void spielerzug() {

        int zug;
        while(true) {
            System.out.println("Es gibt " + steine + " Steine. Bitte nehmen Sie 1,2 oder 3!");
            zug = scanner.nextInt();
            if(zug >= 1 && zug <= 3 ){break;}
            System.out.println("Ungueltiger Zug");
        }
        steine -= zug;
    }
    private void computerzug() {
        int [] zuege = {3,1,1,2};
        if(isGameOver()) {
            System.out.println("Human hat verloren");
            return;
        }
        if(steine == 1) {
            System.out.println("Computer hat verloren");
            steine = 0;
            return;
        }
        int zug = zuege[steine%4];
        System.out.println("Computer nimmt " + zug + " Steine");
        steine-=zug;

    }

    private boolean isGameOver() {
        return steine < 1;
    }
}
