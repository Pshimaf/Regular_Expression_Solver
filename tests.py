import regexps
import unittest


class TestStringMethods(unittest.TestCase):

    def test_expressions(self):
        self.assertRaises(regexps.WrongDivisionNumber, regexps.solver, "aa.", "a", 0)
        self.assertRaises(regexps.WrongMainLetterExpression, regexps.solver, "aa.aa..*", "aa", 9)
        self.assertRaises(regexps.WrongKleeneStarPositionExpression, regexps.solver, "  *aa.", "a", 5)
        self.assertRaises(regexps.WrongRegularExpression, regexps.solver, ".aa.a.", "a", 2)
        self.assertRaises(regexps.WrongRegularExpression, regexps.solver, "aa.a.aa...", "a", 2)
        self.assertRaises(regexps.WrongSymbolError, regexps.solver, "abcde", "a", 2)

    def test_solver(self):
        self.assertEqual(regexps.solver("abc..acb...", "b", 1), True)
        self.assertEqual(regexps.solver("ab + c.aba. * .bac. + . + *", "a", 2), True)
        self.assertEqual(regexps.solver("aa.a.*a.", "a", 3), False)
        self.assertEqual(regexps.solver("a*a.", "a", 100), True)
        self.assertEqual(regexps.solver("aa.*a.aaaa...*.", "a", 4), False)
        self.assertEqual(regexps.solver("aa.*a.aaaa...*.", "a", 5), True)
        self.assertEqual(regexps.solver("aa.*a.aaaa...aa.***..", "a", 8), False)


if __name__ == '__main__':
    unittest.main()
