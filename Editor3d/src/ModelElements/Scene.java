package ModelElements;

import java.util.List;

public class Scene  {

    Integer id;
    public List<PoligonalModel> models;
    public List<Flash> flashes;
    public List<Camera> cameras;

    public Scene(Integer id, List<Flash> flashes, List<PoligonalModel> models, List<Camera> cameras) {
        this.flashes = flashes;
        this.models = models;
        this.cameras = cameras;
        this.id = id;

        this.models.add(new PoligonalModel());  // т.к. 1..* - добавляем 1 эл-т
        this.cameras.add(new Camera());  // т.к. 1..* добавлем 1 элемент

    }

    public <Type> Type method1(Type typeValue){
        Type result = null;
        return result;
    }

    public <Type1, Type2> Type1 method2(Type1 type1Value1, Type2 type2Value2){
        Type1 result = null;
        return result;
    }

}
