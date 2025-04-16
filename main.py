# Example usage 
from pet import Pet

if __name__ == "__main__":
    # Create a pet
    my_pet = Pet("Fluffy")
    
    # Testing basic functionality
    my_pet.get_status()
    my_pet.eat()
    my_pet.play()
    my_pet.sleep()
    my_pet.get_status()
    
    # Testing bonus functionality
    my_pet.train("Sit")
    my_pet.train("Roll over")
    my_pet.train("Play dead")
    my_pet.show_tricks()
    my_pet.get_status() 