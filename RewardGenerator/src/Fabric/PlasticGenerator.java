package Fabric;

import Interface.iGameItem;
import Product.PlasticReward;

public class PlasticGenerator extends ItemGenerator {

    @Override
    public iGameItem CreateItem() {
        return new PlasticReward();
    }
}