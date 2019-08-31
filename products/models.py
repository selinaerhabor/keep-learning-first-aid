from django.db import models

# Model for creating and storing products
class Product(models.Model):
    
    # Dropdown values for Category field in Products Model
    COURSES = 'Courses'
    FA_KITS = 'First Aid Kits'
    BOOKS = 'Books'
    EBOOKS = 'E-Books'
    CDS_DVDS = 'CDs & DVDs'
    MANIKINS = 'Manikins'
    POSTERS = 'Posters'
    EXTRAS = 'Extras'
    
    category_choices = (
        (COURSES, "Courses"),
        (FA_KITS,"First Aid Kits"),
        (BOOKS,"Books"),
        (EBOOKS,"E-Books"),
        (CDS_DVDS,"CDs & DVDs"),
        (MANIKINS,"Manikins"),
        (POSTERS,"Posters"),
        (EXTRAS,"Extras"),
    )
    
    # Dropdown values for Featured field in Home Model
    NONE = 'N'
    HOME = 'H'
    LEARNINGFORKIDS = 'LFK'
    LEARNINGFORADULTS = 'LFA'
    
    featured_choices = (
        (NONE, "No"),
        (HOME, "Home"),
        (LEARNINGFORKIDS, "Learning For Kids"), 
        (LEARNINGFORADULTS, "Learning For Adults"),
    )
    
    INSTOCK = 'In Stock'
    OUTOFSTOCK = 'Out of Stock'
    
    status_choices = (
        (INSTOCK, "In Stock"),
        (OUTOFSTOCK, "Out of Stock"),
    )
    
    id = models.CharField(max_length=20, default='', primary_key='True')
    name = models.CharField(max_length=254, default='')
    category = models.CharField(max_length=250, choices=category_choices, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')
    featured_page = models.CharField(max_length=3, choices=featured_choices, default='N')
    status = models.CharField(max_length=20, choices=status_choices, default='In Stock')

    def __str__(self):
        return "{0}-{1}-{2}-{3}".format(self.category, self.name, self.id, self.featured_page)
