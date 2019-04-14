LCS();
#region "LCS"
        static string res = "";
        public static void LCS()
        {
            string insv = "AGCCCGAATCTAGTAACCCTAAACGCTCAAAATTCCTTAGATAGCTCTCAAGCAGAGTGGCCCTAAAAAGACTAGCCGTGGCCCTCATTATCCCACACCGTCGTCGGACCGGTCGCCCGTTCAATATGGCTGGTTTCGGCTTGCATCGCATGGACCCTCAGCCCCCAGGGCGCTCAATGCCCCAGTGTGTTGGCCGGCAGGTTCCTCAAATATTATCTATGTACATTGCGTGGCGATAGTGAAATCGTAAGTTAGTCCGCCACTGGATGAATACCTAAGGTAGTTTGTACTAGCGCAACTGAGGGGTTACTTCACATAGTGATGCTGACATTTGCCCGCACGCCAAAAGCAGTATATAATGTATCGCGCGTATGTTTAGAAGCGGCCTGCACACGTGCCGAATCCCGGGTAGCTGTAAAGGTGCACATGTGCTCGCACTATTGGACGAGCTTTTGACCATTTAGTGCTTCGCGATAGTTCCGGCTATACTTGAGAAGAAATAACCCTATAACAGCGCTAACCAGTTCAGTCCGATGGCCGCACAAAAGAGGCATTAAAGAAGTATCGTTGCATAACGAGCTTCCCAACATTGATGCGAACTTTCGCCATGGTCTGCTTCAAGTAGCGCGTACGGCCGTAAGTTTGAAAAGCGGCCAGCAGAACTCTCAAAGGAAGCTTAGCCCCATCATGCTATCGGAATCGCTCGCTGGGGAACTTTGGATTCGTCCAAAGGGGGATACTGAACTTCGTCGACAGAGGTGGCGATCGAGTCCTGAACTAGCAATTTTGTCCCGGCTCTGTACAGAGCTAGCAATACCATGGTGTTGAATTTATGCGACTTGGGCAGACATTCTTATTTTACCAAGTATGTCTACTACACGGCGTGCAGTCAGAGGCGAATTCGATGGCACGTCTTGTTAACTTGGTTTATGGCATAGAGCTACCT";
            string intv = "CGTAGGTTTAGACGATTGCTCTCCGCGTTATCCTAGTGAGGACTCCCTATGCAAAAAGCCGAGCAAGACCGCGGCCGTTGGAGAATTCTAGGGTATCTAGTCTGACCGCTAACGTATTAGCGCGGTGGAGGGCGAGCCTTGCCGGTCGATCTAGATGGTGGGGTGAAGGACTGAGCCTATTCTTGCCGCCGAGATAACTTCGTCAAGCTACCGGTGTCAGACGCCCGGGGGAGAACATACCATTTCGGCCACACGGACGGCTATTATCATAGCTGAAGAGGGTTACCGGAGTCATCCGATCAGCGAACATTTTATCAGGACGGGCAGTAACTCCGTCTCAATTAGCTAGGGGTAGAACGAGGTGTTCACATTGTTAGTATGGCAAACAGCTTGTATCTGAATAAGGTGAGTAGTGCTGAACGAGGTTAATTTACCCTTAACCAGAATACGATTGGGAGTAAGACCACTGAGCGCGACGGCTACAACAGTTACCTGAACTTTCCTGGCGGACTGCAGCCTGCCTAGCACGTCCGGTAGTGCGTCCGTCCCTGCGGGGCCTACGTTTATGCTCACATAGGCCGGTATACCTTTGCAGTGCCGGGGCTTTTTACAATACAACACTGATCCATAAGCTACCCTTCGAACACTCTGTATGATCCTGCCCCCCCGAGGTGCAGGGCTGGCATGACGTAAAAAAGATATAGGCCCAAGGCGCTGGTACTCCTACGGCGCGGCGTCAGGAACCTGAGGTCTTAACCACGCTACAGACGGGTCTCGAGTGTAAGACTCATCTTCGCGGCAGCGTTAGCATTGGTACGGCCGACGGCTTCCGTTCTTTTAAGTTGAAGGGCGCGTATGGTAAACGCGGTCC";
            //string insv = "AACCTTGG";
            //string intv = "ACACTGTGA";

            int[,] sa = new int[insv.Length + 1, intv.Length + 1];
            string[,] bt = new string[insv.Length + 1, intv.Length + 1];

            for (int i=0;i<=insv.Length;i++){
                sa[i,0]=0;
                //Console.WriteLine(insv.Substring(i, 1));
            }
            for (int t = 0; t <= intv.Length; t++)
                sa[0, t] = 0;

            for (int s = 0; s <= insv.Length; s++)
                for (int t = 0; t <= intv.Length; t++)
                    bt[s, t] = "-";


            for (int i = 1; i <= insv.Length; i++)
                for (int j = 1; j <= intv.Length; j++)
                {
                    string iv =insv.Substring(i-1, 1);
                    string jv = intv.Substring(j-1, 1);
                    int sij1 = 0;
                    if (iv == jv)
                        sij1 = sa[i - 1, j - 1] + 1;

                    sa[i, j] = Math.Max(sa[i - 1, j], Math.Max(sa[i, j - 1], sij1));
                    if (sa[i, j] == sa[i-1, j])
                        bt[i - 1, j - 1] = "|";
                        //bt[i, j] = "D";
                    else if (sa[i, j] == sa[i, j-1])
                        bt[i - 1, j - 1]= "-";
                        //bt[i, j] = "R";
                    else if (sa[i, j]== (sa[i-1, j-1] + 1))
                        bt[i - 1, j - 1]= "/";
                        //bt[i, j] = "C";
                }

            OUTPUTLCS(bt, insv, insv.Length-1, intv.Length-1);

           Debug.WriteLine(res);
           Console.WriteLine(res);
           Console.ReadLine();
        }

        public static void OUTPUTLCS(string[,] bt, string v, int i, int j)
        {
            if (i == -1 || j == -1)
            {
                //Console.WriteLine(v.Substring(i, 1));
                return;
            }
            if (bt[i, j] == "|")
                OUTPUTLCS(bt, v, i - 1, j);
            else if (bt[i, j] == "-")
                OUTPUTLCS(bt, v, i, j - 1);
            else
            {
                OUTPUTLCS(bt, v, i - 1, j - 1);
                res += v.Substring(i, 1);
                //Console.WriteLine(i);
                //Console.WriteLine(v.Substring(i,1));
                 //v.Substring(i, 1);
                //return v.Substring(i, 1);
            }
        }
        #endregion "LCS"
