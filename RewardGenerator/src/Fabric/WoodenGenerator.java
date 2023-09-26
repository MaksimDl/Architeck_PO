package Fabric;

import Interface.iGameItem;
import Product.WoodenReward;

public class WoodenGenerator extends ItemGenerator {

    @Override
    public iGameItem CreateItem() {
        return new WoodenReward();
    }
}