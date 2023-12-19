grammar SimpleSearchQuery;
/**
 * parser
 */
expr:   term | expr OR_OPERATOR term;
term:   factor | term AND_OPERATOR factor;
factor: keywords | NOT_OPERATOR keywords;
keywords: '(' expr ')' | alphabets;
alphabets: ALPHABETS;

/**
 * lexer
 */
ALPHABETS: [a-z]+ ;
OR_OPERATOR : 'OR';
AND_OPERATOR : 'AND';
NOT_OPERATOR : 'NOT';
WHITE_SPACES : [ \t\n\r]+ -> skip ;
