import unittest
from functions_panda import per_capi, average_year, latest_by_country


class TestMethods(unittest.TestCase):

    def test_by_country(self):
        """This function test latest_by_country.
        With this function we testing the function
        latest_by country.

        We test several returns to see if our function
        returns the right results. If return is ok the
        test return ok
        """

        self.assertEqual({'country': 'Albania', 'year': 2017, 'emissions': 4342.011}, latest_by_country('Albania'))
        self.assertIsNotNone({2005}, latest_by_country('France'))
        self.assertIsNot({1999}, latest_by_country('France'))
        self.assertIsInstance(latest_by_country('Belgium'), dict)

       
    def test_average_for_year (self):
        """This function test average_for_year.
        With this function we testing the function
        average_for_year.

        We test several returns to see if our function
        returns the right results. If return is ok the
        test return ok
        """

        self.assertEqual({"total": 217093.22722535214, "year": 2016}, average_year(2016))
        self.assertIsNotNone(1985 ,average_year(1985))
        self.assertIsNotNone({"year": 1975} ,average_year(1975))
        self.assertIsInstance(average_year(1995), dict)
        self.assertIsNot({2000}, average_year(1995))
        
        
    def test_per_capita (self):
        """ This function test per_capita.
        With this function we testing the function
        per_capita.

        We test several returns to see if our function
        returns the right results. If return is ok the
        test return ok
        """
        self.assertEqual({1975: 2.562, 1985: 3.191, 1995: 2.058, 2005 : 2.22, 2010: 2.604, 2015: 2.342, 2016: 2.422, 2017: 2.283}, per_capi('Cuba'))
        self.assertIsNotNone({2.058}, per_capi('Cuba'))
        self.assertIsNotNone({2010}, per_capi('France'))
        self.assertIsNot({1999}, per_capi('France'))
        self.assertEqual({ 1975: 1.205, 1985: 1.152, 1995: 1.405, 2005: 1.667, 2010: 1.89, 2015: 2.203, 2016: 2.015, 2017: 2.043}, per_capi('Brazil'))
        self.assertIsInstance(per_capi('Belgium'), dict)
        
        
if __name__ == '__main__':
    unittest.main()
