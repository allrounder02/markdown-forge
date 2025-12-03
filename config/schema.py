from typing import Dict, Optional
from pydantic import BaseModel, Field

class Margins(BaseModel):
    top: str = "2cm"
    bottom: str = "2cm"
    left: str = "2cm"
    right: str = "2cm"

class DocumentConfig(BaseModel):
    page_size: str = "A4"
    margins: Margins = Field(default_factory=Margins)

class Fonts(BaseModel):
    body: str = "Roboto"
    heading: str = "Roboto Slab"
    code: str = "Fira Code"
    base_size: str = "11pt"
    line_height: float = 1.5

class TextStyle(BaseModel):
    size: Optional[str] = None
    weight: Optional[str] = None
    color: Optional[str] = None
    style: Optional[str] = None

class Styles(BaseModel):
    h1: TextStyle
    h2: TextStyle
    h3: TextStyle
    h4: TextStyle
    h5: TextStyle
    h6: TextStyle
    body: Optional[TextStyle] = None
    code: Optional[TextStyle] = None

class Config(BaseModel):
    document: DocumentConfig = Field(default_factory=DocumentConfig)
    fonts: Fonts = Field(default_factory=Fonts)
    styles: Styles
