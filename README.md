# 1. Why does SpatialObject own geometry?
## SpatialObject owns the geometry because all spatial classes like Parcel, Building, and Road need it. Instead of repeating geometry in every class, it is placed in one base class so everything stays consistent and organized. This also follows good object-oriented design, where common attributes are centralized in a parent class and inherited by its subclasses.

# 2. Why should distance_to() not be rewritten in every subclass? 
## distance_to() should not be rewritten because it works the same for all spatial objects. Writing it once in SpatialObject avoids repeating code and makes the system easier to maintain. If it is written in every class, the concept of polymorphism is not followed.

# 3. How does this support abstraction and reuse?
## This supports abstraction because subclasses do not need to know how geometry calculations work instead they just use the methods. It supports reuse because the same methods are used by all spatial classes, so you do not have to write them again. This makes the system more efficient, scalable, and easier to maintain, while also ensuring that the implementation closely follows the UML design.

# Part B.4
## In this step, I learned that the constructor (__init__) is where UML attributes are translated into actual object data in Python. Attributes shown in the UML, such as area, height, or income, must be defined as instance variables like self.area, self.height, and self.income so that each object properly stores its state when created. I also understood that values should not be hardcoded outside the constructor because this breaks the connection between the UML design and the implementation.

# Part B Summary
# Briefly explain how the Lecture 6 case study was translated into Python.
## In the Lecture 6 case study, the UML design was translated into Python by first identifying the common features of spatial objects and implementing them in a base class. The SpatialObject class became the parent class, which stores geometry and provides shared spatial methods. The classes Parcel, Building, and Road inherited from this base class since they all represent spatial entities, while Household was implemented as a non-spatial class. Shared methods such as intersects() and distance_to() were placed in SpatialObject so they could be reused by all spatial classes. The relationships defined in the UML were also implemented using object references, where buildings are linked to parcels, households are linked to buildings, and roads are connected to parcels through adjacency. This approach ensured that the Python implementation closely followed the structure and relationships defined in the UML diagram.

# Part C Summary
# Explain how your own UML diagram was translated into code.
## In my own UML diagram, the system was translated into Python by creating each class as a separate part of the program. The classes in my model include Province, Municipality, Barangay, Parcel, TransmissionLineEasement, EasementChecker, RiskAnalyzer, and Report, along with the base class SpatialObject. The UML attributes were turned into object state inside the constructors, such as names for administrative units, geometry for spatial objects, and properties like width and voltage for transmission lines. The UML methods became class behaviors like checking intersections, calculating distance, assessing risk, and generating reports. The relationships were implemented using object references, such as municipalities belonging to provinces, barangays belonging to municipalities, and parcels belonging to barangays. The hardest relationships to implement were the ones involving spatial checking between parcels and transmission line easements because they required careful handling of geometry and interactions between multiple objects.


# Reflection
# 1. What was easier to translate into code: attributes, methods, or inheritance?
## Attributes were the easiest to translate into code because they directly map from the UML diagram to the constructor as instance variables. It was straightforward to convert attributes like area, height, or income into self variables inside the class.

# 2. Which relationship in your UML was hardest to implement?
## The relationships between objects were the hardest to implement, especially linking objects like Building to Parcel or Household to Building. It required careful handling of object references and making sure that each class correctly stored and accessed related objects.

# 3. Did your code exactly match your UML, or did you revise some parts during implementation?
## My code did not exactly match the UML at first, and I had to revise some parts during implementation. Some adjustments were needed to make the relationships work properly and to organize attributes and methods more logically in the code.

# 4. What did you learn about the importance of OOAD from this exercise?
## I learned that OOAD is important because it provides a clear structure before coding, making the implementation more organized and easier to understand. It also helps ensure that classes, attributes, methods, and relationships are properly designed, which leads to cleaner, more maintainable code.