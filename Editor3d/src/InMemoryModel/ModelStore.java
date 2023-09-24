package InMemoryModel;

import ModelElements.Camera;
import ModelElements.Flash;
import ModelElements.PoligonalModel;
import ModelElements.Scene;

import java.util.ArrayList;
import java.util.List;


// хранилище моделей
public class ModelStore implements IModelChanger {

    public ModelStore(IModelChangedObserver[] changeObservers) {
        this.changeObservers = changeObservers;
        this.models = new ArrayList<>();
        this.scenes = new ArrayList<>();
        this.flashes = new ArrayList<>();
        this.cameras = new ArrayList<>();

        models.add(new PoligonalModel());
        scenes.add(new Scene(null,null, null, null));
        flashes.add(new Flash());
        cameras.add(new Camera());
    }

    public List<PoligonalModel> models;
    public List<Scene> scenes;
    public List<Flash> flashes;
    public List<Camera> cameras;
    private IModelChangedObserver[] changeObservers;





    //регистрация изменения
    @Override
    public void NotifyChange(IModelChanger sender) {

    }

    public Scene getScene(Integer id)
    {
        return null;
    }

}
