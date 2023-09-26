package Fabric;

import Interface.iGameItem;

public abstract class ItemGenerator {
    public abstract iGameItem CreateItem();

    public void openReward(){
        CreateItem().open();
    }
}
