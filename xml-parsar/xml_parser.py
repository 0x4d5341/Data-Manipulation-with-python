#!/usr/bin/python3
import xml.etree.ElementTree as ET 
import sys

class XML_parser():
	def __init__(self,xml):
		self.xml = xml 

	def parse(self,parse_type="doc"):
		if parse_type == "doc":
			root = ET.parse(self.xml).getroot()
		else:
			root = ET.fromstring(self.xml)
		tag = root.tag
		print("Root tag is :"+str(tag))
		attributes = root.attrib 
		print("Root attributes are: ")
		for k,v in attributes.items():
			print("\t"+str(k) +" : "+str(v))
		print("\nPrinting Node Details without knowing subtags :")
		for employee in root:
			print("----------------")
			for element in employee:
				ele_name = element.tag
				ele_value = element.find(element.tag)
				print("\t\t"+ele_name, " : ",ele_value)

		print("\nPrinting Node Deatils Specifying Subtags : ")
		for employee in root.findall("employee"):
			print("\n---------------------")
			print("\t\tName : "+str(employee.find("name").text))
			print("\t\tSalary : "+str(employee.find("salary").text))
			print("\t\tManager Id : "+str(employee.find("manager_id").text))
			print("\t\tDOJ : "+str(employee.find("doj").text))

obj = XML_parser(sys.argv[1])
obj.parse()