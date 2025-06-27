# Abstract Class for File Parsers

# Create an abstract class named FileParser with an abstract method parse(data).

# Create concrete classes:

# JSONParser that implements parse(data) method and prints: “Parsing JSON data...”

# XMLParser that implements parse(data) method and prints: “Parsing XML data...”

# Test both classes.
from abc import ABC, abstractmethod

class FileParsers(ABC):
    @abstractmethod
    def parse(self, data):
        pass

class JSONParser(FileParsers):
    def parse(self, data):
        print(data)

class XMLParser(FileParsers):
    def parse(self, data):
        print(data)

JS = JSONParser()
XM = XMLParser()

JS.parse("Parsing JSON data...")
XM.parse("Parsing XML data...")


