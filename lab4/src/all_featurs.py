import unittest
from post_features import suite as post
from comment_feature import suite as comment
from category_features import suite as category
from enquirie_feature import suite as enquirie
from user_feature import suite as user

def suite():
    suite = unittest.TestSuite()

    suite.addTests([post(),comment(),category(),enquirie(),user()])
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())