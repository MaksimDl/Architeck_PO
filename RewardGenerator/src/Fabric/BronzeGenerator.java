package Fabric;

import Interface.iGameItem;
import Product.BronzeReward;

public class BronzeGenerator extends ItemGenerator {

    @Override
    public iGameItem CreateItem() {
        return new BronzeReward();
    }
}