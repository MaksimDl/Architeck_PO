package Fabric;

import Interface.iGameItem;
import Product.SteelReward;

public class SteelGenerator extends ItemGenerator {

    @Override
    public iGameItem CreateItem() {
        return new SteelReward();
    }
}