GREEDYSORTING();

#region "GREEDYSORTING"
        public static void Breakpoints(int[] p )
        {
            //dataset_88_1_0
            int bt = 0;
            //p[p.Length] = p.Length;
            for (int i = -1; i < p.Length; i++)
            {
               //#Console.WriteLine("BT = " + bt + " - " + p[i] + " - " + i);
                if (i == -1)
                {
                    if(0!=p[i+1])
                        bt += 1;
                    //Console.WriteLine("BT = " + bt + " - " + p[i+1] + " - " + "F"+i);
                }
                else if (i == p.Length-1)
                {
                    if (p[i] != p.Length)
                        bt += 1;
                    //Console.WriteLine("BT = " + bt + " - " + p[i] + " - " + "L" +i);
                }
                else if (p[i] != p[i+1]- 1)
                {
                    bt += 1;
                    //Console.WriteLine("BT = " + bt + " - " + p[i] + " - " + "M" + i);
                }

                
            }
            Console.WriteLine("BT = " + bt);
            Console.ReadLine();
        }

        public static void GREEDYSORTING()
        {
            string line, data="";
            StreamReader file = new StreamReader(@"C:\Users\kaderm\Downloads\dataset_88_1_0.txt");
            while ((line = file.ReadLine()) != null)
            {
                line = line.Replace(")","");
                line = line.Replace("(", "");
                data = line;
                //Console.WriteLine(line);
                //string[] sp = line.Split(' ');
            }

            string[] sp = data.Split(' ');
            file.Close();
            int[] p = new int[sp.Length];
            for (int i = 0; i < sp.Length; i++)
            {
                p[i] = Int32.Parse(sp[i]);
                //Console.Write(sp[i] + "~");
            }
            Breakpoints(p);
            System.IO.File.WriteAllText(@"C:\Users\kaderm\Downloads\result.txt", string.Empty);
            int ard = 0;
            int bt = 0;
            //PrintReverse(p, ard);
            //int[] p = { -3,  +4, +1, +5, - 2 };

            for (int i = 0; i < p.Length; i++)
            {
                int pi = System.Math.Abs(p[i]);
                int ipos = i;
                bool reverse = false;
                for (int j = i; j < p.Length; j++)
                {
                    int pj = System.Math.Abs(p[j]);
                    if (pi > pj)
                    {
                        pi = pj;
                        ipos = j;
                        reverse = true;
                    }
                }
                if (reverse)
                {
                    ard += 1;
                    //bt = ard;
                    //Console.WriteLine("BT = " + pi);
                    int[] tp = new int[ipos + 1 - i];
                    int tpi = 0;
                    for (int k = i; k <= ipos; k++)
                    {
                        tp[tpi++] = p[k];
                    }

                    for (int k = 0; k < tp.Length; k++)
                    {
                        p[ipos - k] = tp[k] * -1;
                    }

                    PrintReverse(p, ard);
                }
                if (p[i] < 0)
                {
                    ard += 1;
                    p[i] = p[i] * -1;
                    PrintReverse(p, ard);
                }

            }
            Console.ReadLine();
        }

        public static void PrintReverse(int[] p, int ard)
        {
            Console.WriteLine("ARD = " + ard);
            using (StreamWriter writer = new StreamWriter(@"C:\Users\kaderm\Downloads\result.txt", true))
            {
                for (int i = 0; i < p.Length; i++)
                {
                    string spe = " ";
                    string spo = "";
                    if (i == 0)
                        spo = "(";
                    if (i == p.Length - 1)
                        spe = ")";
                    if (p[i] > 0)
                        writer.Write(spo+"+" + p[i] + spe);
                    else
                        writer.Write(spo + p[i] + spe);
                }
                writer.WriteLine("");
                //if(p[i]>0)
                //    Console.Write("+"+p[i] + " ");
                //else
                //    Console.Write(p[i] + " ");
            }
            //Console.WriteLine("");
            
        }
        #endregion "GREEDYSORTING"
