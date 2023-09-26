package Fabric;

import Interface.iGameItem;
import Product.OreReward;

public class OreGenerator extends ItemGenerator {

    @Override
    public iGameItem CreateItem() {
        return new OreReward();
    }
}