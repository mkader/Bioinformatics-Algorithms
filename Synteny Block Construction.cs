SyntenyBlockConstruction();
#region "SyntenyBlockConstruction"
        public static void SyntenyBlockConstruction()
        {
            DateTime dt0 = DateTime.Now;
            dt0.ToLongTimeString();
            string line = "";
            int count = 0;
            int in_kmer = 0;
            string in_dna0 = "";
            string in_dna1 = "";
            StreamReader file = new StreamReader(@"C:\Users\kaderm\Downloads\w_8_3_dataset6.txt");
            while ((line = file.ReadLine()) != null)
            {
                if (count == 0)
                    in_kmer = Int32.Parse(line);
                else if (count == 1)
                    in_dna0 = line;
                else if (count == 2)
                    in_dna1 = line;
                else
                    break;
                count++;
            }
            string dna1_rev = in_dna1.Replace("A", "0");
            dna1_rev = dna1_rev.Replace("C", "1");
            dna1_rev = dna1_rev.Replace("G", "2");
            dna1_rev = dna1_rev.Replace("T", "3");

            dna1_rev = dna1_rev.Replace("0", "T");
            dna1_rev = dna1_rev.Replace("1", "G");
            dna1_rev = dna1_rev.Replace("2", "C");
            dna1_rev = dna1_rev.Replace("3", "A");
          
            System.IO.File.WriteAllText(@"C:\Users\kaderm\Downloads\result.txt", string.Empty);
            StreamWriter writer = new StreamWriter(@"C:\Users\kaderm\Downloads\result.txt", true);
            
            //new version
            Console.WriteLine(in_dna0.Length);
            Console.WriteLine(in_kmer);
            //writer.WriteLine(in_dna0);
            //writer.WriteLine(in_dna1);
            //writer.WriteLine(dna1_rev);
            //writer.WriteLine(in_dna0);
            string[] sdna0 = new string[in_dna0.Length-in_kmer+1];
            string[] sdna1 = new string[in_dna1.Length - in_kmer + 1];
            string[] sdna1r = new string[in_dna1.Length - in_kmer + 1];
            ArrayList ar = new ArrayList();
            for (int i=0;i<= in_dna0.Length - in_kmer;i++)
            {
                sdna0[i] = in_dna0.Substring(i, in_kmer);
            }
            for (int i = 0; i <= in_dna1.Length - in_kmer; i++)
            {
                sdna1[i] = in_dna1.Substring(i, in_kmer);
                sdna1r[i] = dna1_rev.Substring(i, in_kmer);
            }

            //for (int i = 0; i <= in_dna0.Length - in_kmer; i++)
            for (int i = 0; i < sdna0.Length; i++)
            {
                string dna0 = sdna0[i];
                for (int j = 0; j < sdna1.Length; j++)
                {
                    string dna1 = sdna1[j];
                    if (dna0 == dna1)
                    {
                        //int[] dn = new int[] { i, j };
                        if (!ar.Contains("(" + i + ", " + j + ")"))
                        {
                            ar.Add("(" + i + ", " + j + ")");
                            writer.WriteLine("(" + i + ", " + j + ")");
                        }
                        //writer.WriteLine(i + " - " + dna0 + " - " + j + " - " + dna1);
                    }
                }
                char[] arr = dna0.ToCharArray();
                Array.Reverse(arr);
                dna0 = new string(arr);
                for (int j = 0; j < sdna1r.Length; j++)
                {
                    string dna1 = sdna1r[j];
                    if (dna0 == dna1)
                    {
                        if (!ar.Contains("(" + i + ", " + j + ")"))
                        {
                            ar.Add("(" + i + ", " + j + ")");
                            writer.WriteLine("(" + i + ", " + j + ")");
                        }
                        //writer.WriteLine("R "+i + " - " + dna0 + " - " + j + " - " + dna1);
                    }
                }
            }

            writer.Close();
           
            DateTime dt1 = DateTime.Now;
            Console.WriteLine("Done - " + (dt0-dt1).ToString());
            Console.ReadLine();
        }
        #endregion "SyntenyBlockConstruction"
