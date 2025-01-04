class Recipe:
	def __init__(self, label, image, url, dietLabels, portion, healthLabels, cautions, ingredientLines, calories, totalTime, cuisineType, totalNutrients):
		self.label = label # recipe name
		self.image = image # recipe image
		self.url = url # recipe original website 
		self.dietLabels = dietLabels # e.g: high-fiber/low-sodium
		self.portion = portion # number of portions
		self.healthLabels = healthLabels # e.g: Egg-free/soy-free
		self.cautions = cautions # Tree-Nuts
		self.ingredientLines  = ingredientLines # list of strings of recipe
		self.calories = calories
		self.totalTime = totalTime # time in minutes
		self.cuisineType = cuisineType
		self.totalNutrients = totalNutrients # list of different nutritional facts. e.g: FAT, CHOCDF(carbs), PROCNT(protein)
		self.missingIngredients = []
