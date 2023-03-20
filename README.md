<h1>Vetor.py</h1>
This is an example of a Python implementation of a vector. A vector is a data structure that stores a set of elements in contiguous memory positions. This implementation includes methods to insert, remove, list, and search for elements in a vector.

Usage
To create a new vector, simply instantiate the Vector class and pass the desired size as a parameter:

scss
Copy code
  v = Vector(10)
This will create a vector with capacity for 10 elements.

To insert an element at a specific position in the vector, use the insert_element_position method:

css
Copy code
  v.insert_element_position(element, position)
To insert an element at the end of the vector, use the insert_element_end method:

scss
Copy code
  v.insert_element_end(element)
To remove an element at a specific index, use the remove_element_index method:

perl
Copy code
  v.remove_element_index(index)
To remove a specific element from the vector, use the remove_element method:

scss
Copy code
  v.remove_element(element)
To list an element at a specific position, use the list_element method:

css
Copy code
  v.list_element(position)
To check if a specific element is contained in the vector, use the contains method:

scss
Copy code
  v.contains(element)
To get the size of the vector, use the size method:

scss
Copy code
  v.size()
To print the elements in the vector, use the __str__ method:

scss
Copy code
print(v)
Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue if you encounter a bug or have a suggestion for improvement.

License
This project is licensed under the MIT License - see the LICENSE.md file for details.
