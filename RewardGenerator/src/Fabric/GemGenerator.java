package Fabric;

import Interface.iGameItem;
import Product.GemReward;

public class GemGenerator extends ItemGenerator{

    @Override
    public iGameItem CreateItem() {
        return new GemReward();
    }
}
