#The Adapter design pattern allows the interface of an existing class to be used as another interface. It is often used to make existing classes work with others without modifying their source code.

# Target interface that the client code expects
class Target:
    def request(self):
        pass

# Adaptee (the class to be adapted)
class Adaptee:
    def specific_request(self):
        return "Adaptee's specific request !!"

# Adapter class that makes Adaptee compatible with Target
class Adapter(Target):
    def __init__(self, adaptee):
        self.adaptee = adaptee
    
    def request(self):
        return f"Adapter: {self.adaptee.specific_request()}"

# Client code that expects the Target interface
def client_code(target):
    return target.request()

adaptee = Adaptee()
adapter = Adapter(adaptee)
result = client_code(adapter)
print(result)