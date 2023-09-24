package ModelElements;

import java.util.ArrayList;
import java.util.List;

public class PoligonalModel {

    public PoligonalModel() {

        this.textures = new ArrayList<>();
        this.poligons = new ArrayList<>();
    }

    public List<Poligon> poligons;  // т.к. * - значит список
    public List<Texture> textures; // т.к. * - значит список.


}
