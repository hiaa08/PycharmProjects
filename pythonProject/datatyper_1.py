#int, float og bool, (none)

int_variable = 42
print(int_variable)

float_variable = 3.14
print(float_variable)

bool_true = True
bool_false = False
print(bool_true)
print(bool_false)

none_value = None
print(none_value)

#int(), float(), str(), bool()= konvertering av int til float
float(int_variable)
print(float(int_variable))
print(int(float_variable))  #konvertering fra float til int
"11" #string til tall
print(int("11"))
print(float("11.6"))
print(float("11.6")) #samsvarer ikke med int, error. Kan koncvertere int tekst til float
print(int(bool_true)) #representerer 1
print(int(bool_false)) #representerer 0 verdi i python
