from pydantic import BaseModel as _BaseModel


class _BM(_BaseModel):
  def __repr__(self):
    # Get the class name
    class_name = self.__class__.__name__
    # Get a string of all field names and values, with space separation
    fields_str = " ".join(f"{key}={value!r}" for key, value in self.__dict__.items())
    # Format the string as required
    return f"{class_name}({fields_str})"

# Example usage
class ExampleModel(_BM):
  a: int
  b: int
  c: int

