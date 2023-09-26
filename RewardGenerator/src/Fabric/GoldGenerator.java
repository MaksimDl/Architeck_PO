package Fabric;

import Interface.iGameItem;
import Product.GoldReward;

public class GoldGenerator extends ItemGenerator{
    @Override
    public iGameItem CreateItem() {
        return new GoldReward();
    }
}
