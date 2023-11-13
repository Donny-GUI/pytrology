Definitions = {
    "mineral": "Minerals are natural occurring elements and compounds with a definite homogeneous chemical composition and ordered atomic composition",
    "luster":" Quality of light reflected from the surface of a mineral. Examples are metallic, pearly, waxy, dull.",
    "streak":" Performed by scratching the sample on a porcelain plate. The color of the streak can help name the mineral.",
    "hardness": "The resistance of a mineral to scratching.",
    "cleavage": "A mineral can either show fracture or cleavage, the former being breakage of uneven surfaces, and the latter a breakage along closely spaced parallel planes.",
    "rock":"A rock is any naturally occurring solid mass or aggregate of minerals or mineraloids.",
    
}

class YearsInBillions:
    def __init__(self, value: float) -> None:
        self.value = value
        self.post = "Billion Years Ago"
        


geological_time_scale = {
    "Precambrian": {
        "Hadean": "4.6 - 4 billion years ago",
        "Archean": "4 - 2.5 billion years ago",
        "Proterozoic": "2.5 billion - 541 million years ago"
    },
    "Phanerozoic": {
        "Paleozoic": {
            "Cambrian": "541 - 485.4 million years ago",
            "Ordovician": "485.4 - 443.8 million years ago",
            "Silurian": "443.8 - 419.2 million years ago",
            "Devonian": "419.2 - 358.9 million years ago",
            "Carboniferous": {
                "Mississippian": "358.9 - 323.2 million years ago",
                "Pennsylvanian": "323.2 - 298.9 million years ago"
            },
            "Permian": "298.9 - 251.902 million years ago"
        },
        "Mesozoic": {
            "Triassic": "251.902 - 201.3 million years ago",
            "Jurassic": "201.3 - 145 million years ago",
            "Cretaceous": "145 - 66 million years ago"
        },
        "Cenozoic": {
            "Paleogene": {
                "Paleocene": "66 - 56 million years ago",
                "Eocene": "56 - 33.9 million years ago",
                "Oligocene": "33.9 - 23 million years ago"
            },
            "Neogene": {
                "Miocene": "23 - 5.3 million years ago",
                "Pliocene": "5.3 - 2.6 million years ago"
            },
            "Quaternary": {
                "Pleistocene": "2.6 million - 11.7 thousand years ago",
                "Holocene": "11.7 thousand years ago - Present"
            }
        }
    }
}

moon_geological_time_scale = {
    "Formation": "4.5 billion years ago",
    "Pre-Nectarian": {
        "Pre-Imbrian": {
            "Lower Pre-Imbrian": "4.5 - 3.8 billion years ago",
            "Upper Pre-Imbrian": "3.8 - 3.2 billion years ago"
        },
        "Nectarian": {
            "Lower Nectarian": "3.92 - 3.85 billion years ago",
            "Upper Nectarian": "3.85 - 3.92 billion years ago"
        }
    },
    "Imbrian": {
        "Lower Imbrian": "3.2 - 3 billion years ago",
        "Upper Imbrian": "3 - 1 billion years ago"
    },
    "Eratosthenian": {
        "Lower Eratosthenian": "1 billion - 320 million years ago",
        "Upper Eratosthenian": "320 - 110 million years ago"
    },
    "Copernican": {
        "Lower Copernican": "110 million - 1 million years ago",
        "Upper Copernican": "1 million years ago - Present"
    }
}