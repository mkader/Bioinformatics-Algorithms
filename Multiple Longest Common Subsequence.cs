MultipleLCS();

#region "Multiple Longest Common Subsequence Problem"
        static string in_k = "";
        static string in_s = "";
        static string in_t = "";
        static string mlcs1 = "";
        static string mlcs2 = "";
        static string mlcs3 = "";
        static int mcount = 0;
        public static void MultipleLCS()
        {
            DateTime dt0 = DateTime.Now;
            dt0.ToLongTimeString();
            string line = "";
            int count = 0;
            StreamReader file = new StreamReader(@"C:\Users\kaderm\Downloads\w_7_7_dataset4.txt");

            while ((line = file.ReadLine()) != null)
            {
                if (count == 0)
                {
                    in_k = line;
                }
                else if (count == 1)
                {
                    in_s = line;
                }
                else if (count == 2)
                {
                    in_t = line;
                }
                else
                    break;
                count++;
            }

            Console.WriteLine(in_k);
            Console.WriteLine(in_s);
            Console.WriteLine(in_t);

            int kl = in_k.Length;
            int sl = in_s.Length;
            int tl = in_t.Length;


            int[, ,] dist = new int[kl + 1, sl + 1, tl + 1];
            string[, ,] back = new string[kl + 1, sl + 1, tl + 1];
            for (int i = 0; i <= kl; i++)
            {
                for (int j = 0; j <= sl; j++)
                {
                    for (int k = 0; k <= tl; k++)
                    {
                        dist[i,j,k] = 0;
                        back[i, j, k] = "0";
                    }
                }
            }

            for (int i = 0; i <= kl; i++)
            {
                for (int j = 0; j <= sl; j++)
                {
                        dist[i, j, 0] = 1;
                }
            }

            for (int i = 0; i <= kl; i++)
            {
                for (int k = 0; k <= tl; k++)
                {
                    dist[i, 0, k] = 1;
                }
            }

            //for (int i = 0; i <= insv.Length; i++)
            //{
            //    sa[i, 0] = 0;
            //    //Console.WriteLine(insv.Substring(i, 1));
            //}
            //for (int t = 0; t <= intv.Length; t++)
            //    sa[0, t] = 0;

            System.IO.File.WriteAllText(@"C:\Users\kaderm\Downloads\result.txt", string.Empty);
            StreamWriter writer = new StreamWriter(@"C:\Users\kaderm\Downloads\result.txt", true);

            //PrintMatrix(writer, dist, kl, sl, tl);

            //writer.WriteLine("");

            for (int i = 1; i <= kl; i++)
            {
                string iv = in_k.Substring(i - 1, 1);
                for (int j = 1; j <= sl; j++)
                {
                    string jv = in_s.Substring(j - 1, 1);
                    for (int k = 1; k <= tl; k++)
                    {
                        string kv = in_t.Substring(k - 1, 1);

                        int di1jk = dist[i - 1, j, k] + score(iv,"-","-");
                        int dij1k = dist[i, j - 1, k] + score("-", jv, "-");
                        int dijk1 = dist[i, j, k - 1] + score("-", "-", kv);
                        int di1j1k = dist[i - 1, j - 1, k] + +score(iv, jv, "-");
                        int di1jk1 = dist[i - 1, j, k - 1] + score(iv, "-", kv);
                        int dij1k1 = dist[i, j - 1, k - 1] + score("-", jv, kv);
                        int di1j1k1 = dist[i - 1, j - 1, k - 1] + score(iv, jv, kv);

                        int[] mv = new int[]{di1jk,dij1k,dijk1,di1j1k,di1jk1,dij1k1,di1j1k1};

                        dist[i, j, k] = mv.Max();

                        //if (dist[i, j, k] == di1j1k1)
                        //    back[i - 1, j - 1, k - 1] = "7";
                        //else if (dist[i, j, k] == dij1k1)
                        //    back[i - 1, j - 1, k - 1] = "6";
                        //else if (dist[i, j, k] == di1jk1)
                        //    back[i - 1, j - 1, k - 1] = "5";
                        //else if (dist[i, j, k] == di1j1k)
                        //    back[i - 1, j - 1, k - 1] = "4";
                        //else if (dist[i, j, k] == dijk1)
                        //    back[i - 1, j - 1, k - 1] = "3";
                        //else if (dist[i, j, k] == dij1k)
                        //    back[i - 1, j - 1, k - 1] = "2";
                        ////else if (dist[i, j, k] == di1j1k1)
                        //else
                        //    back[i - 1, j - 1, k - 1] = "1";

                        if (dist[i, j, k] == di1jk)
                            back[i- 1, j - 1, k - 1] = "1";
                        else if (dist[i, j, k] == dij1k)
                            back[i - 1, j - 1, k - 1] = "2";
                        else if (dist[i, j, k] == dijk1)
                            back[i - 1, j - 1, k - 1] = "3";
                        else if (dist[i, j, k] == di1j1k)
                            back[i - 1, j - 1, k - 1] = "4";
                        else if (dist[i, j, k] == di1jk1)
                            back[i - 1, j - 1, k - 1] = "5";
                        else if (dist[i, j, k] == dij1k1)
                            back[i - 1, j - 1, k - 1] = "6";
                        //else if (dist[i, j, k] == di1j1k1)
                        else
                            back[i - 1, j - 1, k - 1] = "7";

                        //writer.Write(i + "," + j + "," + k + " => ");
                        //writer.Write(di1jk);
                        //writer.Write(dij1k);
                        //writer.Write(dijk1);
                        //writer.Write(di1j1k);
                        //writer.Write(di1jk1);
                        //writer.Write(dij1k1);
                        //writer.Write(di1j1k1);
                        //writer.WriteLine(" = "+dist[i, j, k]);
                    }
                    //writer.WriteLine("");
                }
            }

            writer.WriteLine("");
            PrintMatrix(writer, dist, kl, sl, tl);

            writer.WriteLine("");

            for (int i = 0; i < kl; i++)
            {
                //writer.Write(i + " ");
                for (int j = 0; j < sl; j++)
                {
                    writer.Write(i + ","+ j + " => ");
                    //writer.Write(j + "  ");
                    for (int k = 0; k < tl; k++)
                    {
                        //writer.Write(i + ","+ j + "," + k + " => ");
                        writer.Write(back[i, j, k]);
                    }
                    writer.WriteLine("");
                }
                //writer.WriteLine("");
            }

            writer.WriteLine("");
            //PrintMatrix(writer, back, kl, sl, tl);
            //writer.WriteLine("");
            OUTPUTMLCS(writer, back, kl-1, sl-1, tl-1);
            writer.WriteLine("");
            writer.WriteLine(mcount);
            writer.WriteLine(mlcs1);
            writer.WriteLine(mlcs2);
            writer.WriteLine(mlcs3);


            writer.Close();


            DateTime dt1 = DateTime.Now;
            Console.WriteLine("Done - " + (dt0 - dt1).ToString());
            Console.ReadLine();
        }

       
        //static string mlcs = "";
        //static string mlcs = "";
        public static void OUTPUTMLCS(StreamWriter writer, string[, ,] bt, int i, int j, int k)
        {
            writer.Write((i+1) + " - " + (j+1) + " - " + (k+1) + " - " );
            
            if (i == -1 || j == -1 || k==-1)
            //if (i == 0 || j == 0 || k == 0)
            {
                int start = 0;
                if (i > j && i > k)
                    start = i;
                else if (j > i && j > k)
                    start = j;
                else if (k > i && k > j)
                    start = j;

                string s1 = "-";
                string s2 = "-";
                string s3 = "-";
                for (int i1 = start; i1 >= 0; i1--)
                {
                    if (i < 0)
                        mlcs1 = "-" + mlcs1;
                    else
                    {
                        s1 = in_k.Substring(i1, 1);
                        mlcs1 = s1 + mlcs1;
                    }
                }
                for (int i1 = start; i1 >= 0; i1--)
                {
                    if (j < 0)
                        mlcs2 = "-" + mlcs2;
                    else
                    {
                        s2 = in_s.Substring(i1, 1);
                        mlcs2 = s2 + mlcs2;
                    }
                }
                for (int i1 = start; i1 >= 0; i1--)
                {
                    if (k < 0)
                        mlcs3 = "-" + mlcs3;
                    else
                    {
                        s3 = in_t.Substring(i1, 1);
                        mlcs3 = s3 + mlcs3;
                        
                    }
                }

                
                //if (s1 == s2 && s2 == s3)
                //    mcount++;
                return;
            }
            //if (j < 0)
            //    j = 0;
            writer.WriteLine(bt[i, j, k]);
            if (bt[i, j, k] == "1")
            {
                mlcs1 = in_k.Substring(i, 1) + mlcs1;
                mlcs2 = "-" + mlcs2;
                mlcs3 = "-" + mlcs3;
                OUTPUTMLCS(writer,bt, i - 1, j, k);
            }
            else if (bt[i, j, k] == "2")
            {
                mlcs1 = "-" + mlcs1;
                mlcs2 = in_s.Substring(j, 1) + mlcs2;
                mlcs3 = "-" + mlcs3;
                OUTPUTMLCS(writer, bt, i, j - 1, k);
            }
            else if (bt[i, j, k] == "3")
            {
                mlcs1 = "-" + mlcs1;
                mlcs2 = "-" + mlcs2;
                mlcs3 = in_t.Substring(k, 1) + mlcs3;
                OUTPUTMLCS(writer, bt, i, j, k - 1);
            }
            else if (bt[i, j, k] == "4")
            {
                mlcs1 = in_k.Substring(i, 1) + mlcs1;
                mlcs2 = in_s.Substring(j, 1) + mlcs2;
                mlcs3 = "-" + mlcs3;
                OUTPUTMLCS(writer, bt, i - 1, j - 1, k);
            }
            else if (bt[i, j, k] == "5")
            {
                //mlcs += in_k.Substring(i - 1, 1) + "-" + in_t.Substring(k - 1, 1);
                mlcs1 = in_k.Substring(i, 1) + mlcs1;
                mlcs2 = "-" + mlcs2;
                mlcs3 = in_t.Substring(k, 1) + mlcs3;
                //writer.WriteLine(mlcs1 + " - " + mlcs2 + " - " + mlcs3);
                OUTPUTMLCS(writer, bt, i - 1, j, k - 1);
            }
            else if (bt[i, j, k] == "6")
            {
                //mlcs += "-" + in_s.Substring(j - 1, 1) + in_t.Substring(k - 1, 1);
                mlcs1 = "-"+mlcs1;
                mlcs2 = in_s.Substring(j, 1) + mlcs2;
                mlcs3 = in_t.Substring(k, 1) + mlcs3;
                //writer.WriteLine(mlcs1 + " - " + mlcs2 + " - " + mlcs3);
                OUTPUTMLCS(writer, bt, i, j - 1, k - 1);
            }
            else if (bt[i, j, k] == "7")
            {
                //mlcs += in_k.Substring(i - 1, 1)  + in_s.Substring(j - 1, 1) + in_t.Substring(k - 1, 1);
                string s1 = in_k.Substring(i, 1);
                string s2 = in_s.Substring(j, 1);
                string s3 = in_t.Substring(k, 1);
                if (s1 == s2 && s2 == s3)
                    mcount++;
                mlcs1 = in_k.Substring(i, 1) + mlcs1;
                mlcs2 = in_s.Substring(j, 1) + mlcs2;
                mlcs3 = in_t.Substring(k, 1) + mlcs3;
                //writer.WriteLine(count);
                OUTPUTMLCS(writer, bt, i - 1, j - 1, k - 1);
            }
        }


        private static int score(string s, string k, string t)
        {
            if(s==k && k==t && t==s)
                return 1;
            return 0;
        }

        private static void PrintMatrix(StreamWriter writer, int[, ,] m, int kl, int sl, int tl)
        {
            for (int i = 0; i <= kl; i++)
            {
                for (int j = 0; j <= sl; j++)
                {
                    writer.Write(i + "," +j + ", => ");
                    for (int k = 0; k <= tl; k++)
                    {
                        writer.Write(m[i, j, k]);
                    }
                    writer.WriteLine("");

                }
                writer.WriteLine("");
            }
        }
        #endregion
