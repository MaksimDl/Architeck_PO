package InMemoryModel;

//интерфейс смены модели
public interface IModelChanger {
    public void NotifyChange(IModelChanger sender);
}
