import java.util.ArrayList;
import java.util.List;
import java.util.Random;
import java.util.concurrent.ThreadLocalRandom;

import Fabric.BronzeGenerator;
import Fabric.GemGenerator;
import Fabric.GoldGenerator;
import Fabric.ItemGenerator;
import Fabric.OreGenerator;
import Fabric.PlasticGenerator;
import Fabric.SilverGenerator;
import Fabric.SteelGenerator;
import Fabric.WoodenGenerator;

public class Main {
    public static void main(String[] args) {

        ItemGenerator f1 = new GemGenerator();
        f1.openReward();
        ItemGenerator f2 = new GoldGenerator();
        f2.openReward();
        ItemGenerator f3 = new SilverGenerator();
        f3.openReward();

        ItemGenerator f4 = new WoodenGenerator();
        f4.openReward();
        ItemGenerator f5 = new PlasticGenerator();
        f5.openReward();
        ItemGenerator f6 = new OreGenerator();
        f6.openReward();
        ItemGenerator f7 = new SteelGenerator();
        f7.openReward();
        ItemGenerator f8 = new BronzeGenerator();
        f8.openReward();

        List<ItemGenerator> itemGeneratorList = new ArrayList<>();
        itemGeneratorList.add(f1);
        itemGeneratorList.add(f2);
        itemGeneratorList.add(f3);
        itemGeneratorList.add(f4);
        itemGeneratorList.add(f5);
        itemGeneratorList.add(f6);
        itemGeneratorList.add(f7);
        itemGeneratorList.add(f8);
        System.out.println("Now lets random generate rewards. ratio: 1gem, 3 gold, 10 -others");

        Random random = ThreadLocalRandom.current();
        for (int i = 0; i < 10; i++) {
            Integer randInt = random.nextInt(14); // here is magic number - Antipattern
            // should count total ammount and divide. But have no time todo.
            if (randInt < 1) {
                itemGeneratorList.get(0).openReward(); // gew reward. Chance 1/14
            } else if (randInt > 0 && randInt < 4) {
                itemGeneratorList.get(1).openReward(); // gold reward. Chance 3/14
            } else {
                int min = 3; // not sure if have rand range in java
                int max = 8;
                itemGeneratorList.get(random.nextInt(max - min) + min).openReward();
            }
        }

    }
}
