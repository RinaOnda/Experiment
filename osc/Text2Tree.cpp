//create trees from txt files


std::vector<std::string> split(const std::string &str, char sep);
double Convert2Charge(double x);

void Text2Tree(std::string filename){
   std::ifstream fin;
   fin.open(filename.c_str());

   double charge;
   TTree *tree = new TTree("tree","tree");
   tree->Branch("charge", &charge);
   while(fin >> charge){
      charge = Convert2Charge(charge);
      tree->Fill();
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
