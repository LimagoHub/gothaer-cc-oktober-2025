package app;

import client.Client;
import de.bagoit.game.Game;
import de.bagoit.game.nimgame.Nimgame;

public class Main {

    public static void main(String[] args) {

        Game game = new Nimgame();
        Client client = new Client(game);
        client.go();
    }
}
