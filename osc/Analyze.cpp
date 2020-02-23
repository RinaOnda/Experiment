//analyze waveforms

std::vector<std::string> split(const std::string &str, char sep);
double Convert2Charge(double x);
double Integrate(int n, double* x, double* y);
void Draw(int n, double* x, double* y);

void Analyze(std::string filename, std::string opt=""){
   const int nSGP = 998;//set the number of data points
   std::ifstream fin;
   fin.open(filename.c_str());

   int n = 0;
   double x;
   double charge;
   TTree *tree = new TTree("tree","tree");
   tree->Branch("charge", &charge);
   bool first = true;
   double s[nSGP+1], V[nSGP];
   while(fin >> x){
      if(first){
         s[n] = x;
         if(++n==nSGP+1){
            n = 0;
            first = false;
         }
      }else{
         V[n] = x;
         if(++n==nSGP){
            if(opt=="DRAW"){
               Draw(n, s, V);
               return;
            }
            charge = Integrate(n, s, V);
            charge = Convert2Charge(charge);
            tree->Fill();
            n = 0;
         }
      }
   }
   fin.close();

   filename = split(filename, '.')[0] + ".root";
   TFile *fout = new TFile(filename.c_str(), "RECREATE");
   tree->Write();
   fout->Close();
   
}

std::vector<std::string> split(const std::string &str, char sep)
{
    std::vector<std::string> v;
    auto first = str.begin();
    while( first != str.end() ) {
        auto last = first; 
        while( last != str.end() && *last != sep )
            ++last;
        v.push_back(std::string(first, last)); 
        if( last != str.end() )
            ++last;
        first = last; 
    }
    return v;
}

double Convert2Charge(double x){
   const double second = 1.;
   const double electronvolt = 1.e-9;
   const double q = 1.602176634e-19;//C
   const double eplus = 1e-9;
   const double coulomb = eplus/q; 
   const double volt = electronvolt/eplus;
   const double ampere = coulomb/second;
   const double ohm = volt/ampere;
   const double R = 50*ohm;//ohm

   double y = x / R;//V*s --> C

   return y;
}

double Integrate(int n, double* x, double* y){
   const int nPt = 10;
   double baseline = 0;
   double sum = 0;
   for(int i=0; i<n; ++i){
      if(i<nPt){
         baseline += y[i];
         if(i==nPt-1) baseline /= nPt;
      }else sum += (y[i] - baseline) * (x[i+1] - x[i]); 
   }
   return sum;
}

void Draw(int n, double* x, double* y){
   std::cout << n << std::endl;
   TGraph *g = new TGraph(n, x, y);
   g->Draw("APL");
   //delete g;
}
