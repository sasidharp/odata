# Author : Sasidhar@gmail.com
# Project demo library for Odata consumption and creation in python
# EDM CSDL 2.3


# Base Element for all the elements in the EDM model
class Element(object):
    pass

# Root Element
class edmx(Element):

    _attributes = []

    #Contains zero or more edmx:Reference elements
    _references = []

    #MUST contain a single direct child edmx:DataServices element.
    _dataservices = None


    def __init__(self):
        pass

    #get xmlmns , if there is none , return error
    def get_xmlmns(self):
        return self._attributes['XMLMNS']

    #get version , if there is none , return error
    def get_version(self):
        return self._attributes['VERSION']

    #Set the properties XLMNS and VERSION
    def set_property_attribute(self, xmlmns, version, **kwargs):
        #Both are constants and no validation is needed here
        self._attributes['XMLMNS']  = xmlmns
        self._attributes['VERSION'] = version
        #if needed to be changed or modified
        for attr in kwargs:
            if attr in self._attributes:
               self._attributes.remove(attr)
               self._attributes.append(attr)
            else:
                self._attributes.append(attr)

    #Get the refernces
    @property
    def references(self):
        return self._references
    @references.setter
    def references(self, value):
        self._references = value
    @references.deleter
    def references(self):
        del self._references


#Edm Data Services
class edmDataservices(Element):
#Return the type of the element
#Edm Schemas
    schemas = []
#Return the schemas
    def get_schemas(self):
        if not self.schemas is None:
            return self.schemas
        else:
            return None

#Edmx Referemce Elements
class edmReference(Element):
    #Attribute URI
    Uri= {}

#Edmx Include Elements
class edmInclude(Element):
    #Set the namespace and the alias for the include
    def __init__(self,  namespace,  alias):
        self._namespace = namespace
        self._alias = alias
    # properties for namespace
    @property
    def namespace(self):
        return self.namespace
    @namespace.setter
    def namespace(self,value):
        self.namespace = value
    @namespace.deleter
    def namespace(self):
        del self.namespace
    # properties for alias
    @property
    def alias(self):
        return self.alias
    @alias.setter
    def alias(self,value):
        self.alias = value
    @alias.deleter
    def alias(self):
        del self.alias

# edmx:IncludeAnnotations
class edmxIncludeAnnotations(Element):

    _attributes = {}

    def __init__(self,termnamespace,qualifier=None , targetnamespace=None):
        self.attributes['TermNamespace'] = termnamespace
        self.attributes['Qualifier'] = qualifier
        self.attributes['TargetNamespace'] = targetnamespace
        if self.attributes['TargetNamespace'] == "" or self.attributes['TargetNamespace'] != "Validation"
#       return proper error



# # The edm:Schema element contains one or more of the following elements:
#  edm:Action
#  edm:Annotations
#  edm:Annotation
#  edm:ComplexType
#  edm:EntityContainer
#  edm:EntityType
#  edm:EnumType
#  edm:Function
#  edm:Term
#  edm:TypeDefinition
# Values of the Name attribute MUST be unique across all direct child elements of a schema, with the sole
# exception of overloads for an action and overloads for a function. The names are local to the schema;
# they need not be unique within a document.
# Attribute Namespace
# Attribute Alias
class edmSchema(Element):

    _attributes = {}

    _Action = []
    _Annotations = []
    _Annotation = []
    _ComplexType = []
    _EntityContainer = []
    _EntityType = []
    _EnumType = []
    _Function = []
    _Term = []
    _TypeDefinition = []

    # Initialize the object
    def __init__(self, namespace, alias):
        self._attributes['Namespace'] = namespace
        self._attributes['Alias'] = alias

    # Return the namespace
    def get_namespace(self):
        return self._attributes['Namespace']

    # Return alias
    def get_alias(self):
        return self._attributes['Alias']

    # Return Actions if present , if not return none
    def get_actions(self):
        if self._Action is not None: return self._Action, None

    # Return Annotations if present , if not return none
    def get_annotations(self):
        if self._Annotations is not None: return self._Annotations, None

    # Return Annotation if present , if not return none
    def get_annotation(self):
        if self._Annotation is not None: return self._Annotation, None

    # Return complex types if present , if not return none
    def get_complextype(self):
        if self._complexType is not None: return self._complexType, None

#   Return entity container if present , if not return none
    def get_entitycontainer(self):
        if self._EntityContainer is not None: return self._EntityContainer, None

#   Return entity type if present , if not return none
    def get_entitytype(self):
        if self._EntityType is not None: return self._EntityType, None

#   Return Enum type if present , if not return none
    def get_enumtype(self):
        if self._EnumType is not None: return self._EnumType, None

#   Return Function type if present , if not return none
    def get_function(self):
        if self._Function is not None: return self._Function, None

#   Return Term type if present , if not return none
    def get_term(self):
        if self._Term is not None: return self._Term, None

#   Return Term type if present , if not return none
    def get_termdef(self):
        if self._Term_TypeDefinition is not None: return self._TypeDefinition, None



class edmProperty(Element):

    _attributes = {}

    _attributes['Name'] = None
    _attributes['Type'] = None
    _attributes['Nullable'] = None
    _attributes['MaxLength'] = None
    _attributes['Precision'] = None
    _attributes['Scale'] = None
    _attributes['Unicode'] = None
    _attributes['SRID'] = None
    _attributes['DefaultValue'] = None


    def __init__(self):
        pass

    #Set the properties
    def set_property_attribute(self, args, *kwargs):
        pass

    def get_name(self):
        return self._attributes['Name']

    def get_type(self):
        return self._attributes['Type']

    def is_nullable(self):
        return self._attributes['Nullable']

    def get_maxlength(self):
        return self._attributes['MaxLength']

    def get_precision(self):
        return self._attributes['Precision']

    def get_scale(self):
        return self._attributes['Scale']

    def get_Unicode(self):
        return self._attributes['Unicode']

    def get_SRID(self):
        return self._attributes['SRID']




class edmNavigationProperty(Element):

    _attributes = {}


    def __init__(self):
        pass

    #Set the properties
    def set_property_attribute(self, args, *kwargs):
        pass

    def get_name(self):
        return self._attributes['Name']

    def get_type(self):
        return self._attributes['Type']

    def is_numllable(self):
        return self._attributes['Nullable']

    def get_partner(self):
        return self._attributes['Partner']

    def is_containstarget(self):
        return self._attributes['ContainsTarget']


class edmReferentialConstraint(Element):

    _attributes = {}


    def __init__(self):
        pass

    #Set the properties
    def set_property_attribute(self, args, *kwargs):
        pass

    def get_property(self):
        return self._attributes['Property']

    def get_referencedproperty(self):
        return self._attributes['ReferencedProperty']

class edmOnDelete(Element):

    _attributes = {}


    def __init__(self):
        pass

    #Set the properties
    def set_property_attribute(self, args, *kwargs):
        pass

    def get_action(self):
        return self._attributes['Action']

class edmEntityType(Element):

    _attributes = {}


    def __init__(self):
        pass

    #Set the properties
    def set_property_attribute(self, args, *kwargs):
        pass

    def get_name(self):
        return self._attributes['Name']

    def get_baseType(self):
        return self._attributes['BaseType']

    def get_abstract(self):
        return self._attributes['Abstract']

    def get_opentype(self):
        return self._attributes['OpenType']

    def get_hasstream(self):
        return self._attributes['HasStream']


class edmKey(Element):

    def __init__(self):
        pass

   #Set the properties
    def set_property_attribute(self, args, *kwargs):
        pass

class edmPropertyRef(Element):

    def __init__(self):
        pass

   #Set the properties
    def set_property_attribute(self, args, *kwargs):
        pass

    def get_name(self):
        return self._attributes['Name']

    def get_alias(self):
        return self._attributes['Alias']

class edmComplexType(Element):

    def __init__(self):
        pass

   #Set the properties
    def set_property_attribute(self, args, *kwargs):
        pass

    def get_name(self):
        return self._attributes['Name']

    def get_basetype(self):
        return self._attributes['BaseType']

    def get_abstract(self):
        return self._attributes['Abstract']

    def get_opentype(self):
        return self._attributes['OpenType']

class edmEnumType(Element):

    def __init__(self):
        pass

   #Set the properties
    def set_property_attribute(self, args, *kwargs):
        pass

    def get_name(self):
        return self._attributes['Name']

    def get_underlyingtype(self):
        return self._attributes['UnderlyingType']

    def IsFlags(self):
        return self._attributes['IsFlags']

class edmMember(Element):

    def __init__(self):
        pass

   #Set the properties
    def set_property_attribute(self, args, *kwargs):
        pass

    def get_name(self):
        return self._attributes['Name']

    def get_value(self):
        return self._attributes['Value']

class edmTypeDefinition(Element):

    def __init__(self):
        pass

   #Set the properties
    def set_property_attribute(self, args, *kwargs):
        pass

    def get_name(self):
        return self._attributes['Name']

    def get_underlyingtype(self):
        return self._attributes['UnderlyingType']

    def get_maxlength(self):
        return self._attributes['MaxLength']

    def get_precision(self):
        return self._attributes['Precision']

    def get_scale(self):
        return self._attributes['Scale']

    def get_Unicode(self):
        return self._attributes['Unicode']

    def get_SRID(self):
        return self._attributes['SRID']

class edmAction(Element):

    def __init__(self):
        pass

   #Set the properties
    def set_property_attribute(self, args, *kwargs):
        pass

    def get_name(self):
        return self._attributes['Name']

    def is_bound(self):
        return self._attributes['IsBound']

    def EntitySetPath(self):
        return self._attributes['EntitySetPath']

class edmFunction(Element):

    def __init__(self):
        pass

   #Set the properties
    def set_property_attribute(self, args, *kwargs):
        pass

    def get_name(self):
        return self._attributes['Name']

    def is_bound(self):
        return self._attributes['IsBound']

    def IsComposable(self):
        return self._attributes['IsComposable']

    def EntitySetPath(self):
        return self._attributes['EntitySetPath']

class edmReturnType(Element):

    def __init__(self):
        pass

   #Set the properties
    def set_property_attribute(self, args, *kwargs):
        pass

    def get_name(self):
        return self._attributes['Name']

    def is_nullable(self):
        return self._attributes['Nullable']

class edmParameter(Element):

    def __init__(self):
        pass

   #Set the properties
    def set_property_attribute(self, args, *kwargs):
        pass

    def get_name(self):
        return self._attributes['Name']

    def get_type(self):
        return self._attributes['Type']

    def is_nullable(self):
        return self._attributes['Nullable']

    def get_maxlength(self):
        return self._attributes['MaxLength']

    def get_precision(self):
        return self._attributes['Precision']

    def get_scale(self):
        return self._attributes['Scale']

    def get_SRID(self):
        return self._attributes['SRID']

class edmEntityContainer(Element):

    def __init__(self):
        pass

   #Set the properties
    def set_property_attribute(self, args, *kwargs):
        pass

    def get_name(self):
        return self._attributes['Name']

    def get_extends(self):
        return self._attributes['Extends']

class edmEntitySet(Element):

    def __init__(self):
        pass

   #Set the properties
    def set_property_attribute(self, args, *kwargs):
        pass

    def get_name(self):
        return self._attributes['Name']

    def get_extends(self):
        return self._attributes['EntityType']

    def IncludeInServiceDocument(self):
        return self._attributes['IncludeInServiceDocument']

class edmSingleton(Element):

    def __init__(self):
        pass

   #Set the properties
    def set_property_attribute(self, args, *kwargs):
        pass

    def get_name(self):
        return self._attributes['Name']

    def get_type(self):
        return self._attributes['Type']


class edmNavigationPropertyBinding(Element):

    def __init__(self):
        pass

   #Set the properties
    def set_property_attribute(self, args, *kwargs):
        pass

    def get_Path(self):
        return self._attributes['Path']

    def get_Target(self):
        return self._attributes['Target']

class edmActionImport(Element):

    def __init__(self):
        pass

   #Set the properties
    def set_property_attribute(self, args, *kwargs):
        pass

    def get_name(self):
        return self._attributes['Name']

    def get_action(self):
        return self._attributes['Action']

    def get_entityset(self):
        return self._attributes['EntitySet']

class edmFunctionImport(Element):

    def __init__(self):
        pass

   #Set the properties
    def set_property_attribute(self, args, *kwargs):
        pass

    def get_name(self):
        return self._attributes['Name']

    def get_function(self):
        return self._attributes['Function']

    def get_entityset(self):
        return self._attributes['EntitySet']

    def IncludeInServiceDocument(self):
        return self._attributes['IncludeInServiceDocument']



class Documentation(object):
    pass


# EDM CSDL 2.3
# EDM Documentation element , can have only only summary and only one long description
# A model element MUST NOT contain more than one documentation element.

class Documentation_Impl(Documentation):
    def __init__(self):
        self._summary = None
        self._long_description = None
    @property
    def summary(self):
        return self._summary

    @summary.setter
    def summary(self, value):
        self._summary = value

    @summary.deleter
    def summary(self):
        del self._summary

    @property
    def long_description(self):
        return self._long_description

    @long_description.setter
    def long_description(self, value):
        self._long_description = value

    @long_description.deleter
    def long_description(self):
        del self._long_description

    def is_summary_avl(self):
        if not self._summary is None:
            return True
        else:
            return False

    def is_long_description_avl(self):
        if not self._long_description is None:
            return True
        else:
            return False

