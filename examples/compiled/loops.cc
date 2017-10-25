int main()
{
  int j1 = 0;
  int j2 = 0;
  for (int i = 0; i < 100; ++i)
  {
    j1 = j1 + i;
    j2 += i;
  }
  int i2 = 0;
  j1 = 0;
  do 
  {
    j1 += i2;
    i2++;
  } 
  while(i2 < 100);
  return 0;
}
