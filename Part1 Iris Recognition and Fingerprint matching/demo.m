i=imread('D:/College/BE project/Dataset/MMU-Iris-Database/1/left/aeval1.bmp');
subplot(1,2,1);
imshow(i);
title('STEP:1 Image Aquisition(Original Image:1)');

ii=imread('D:/College/BE project/Dataset/MMU-Iris-Database/1/left/aeval3.bmp');
subplot(1,2,2);
imshow(ii);
title('STEP:1 Image Aquisition(Original Image:2)');
figure();

% STEP:2 GRAY SCALE CONVERTION*********************************************

g =rgb2gray(i);
subplot(1,2,1);
imshow(g);
title('STEP:2 Converting into Gray Image:1');

gg=rgb2gray(ii);
subplot(1,2,2);
imshow(gg);
title('STEP:2 Converting into Gray Image:2');
figure();

%crop image
c=imcrop(g,[65,45,190,150]);
subplot(1,2,1);
imshow(c);
title('STEP:2.2 Crop Image:1');

cc=imcrop(gg,[65,45,190,150]);
subplot(1,2,2);
imshow(cc);
title('STEP:2.2 Crop Image:2');

figure();

% Find HISTOGRAM of the Image**********************************************
%imhist works with only 8 bit images
% Hence convert the image to unsigned 8 bit image and plot the histogram
 
z=double(c);
subplot(1,2,1);
imhist(c);
axis off, axis tight;
title('STEP:3 Histogram of the Image:1');

zz=double(cc);
subplot(1,2,2);
imhist(cc);
axis off, axis tight;
title('STEP:3 Histogram of the Image:1');

figure();

% STEP:4 IMAGE SMOOTHING***************************************************

s= fspecial('gaussian',3);
f = imfilter(c,s); 
subplot(1,2,1);
imshow(f,[]),title('STEP:4 Using Gaussian Filter Smoothing Image:1 ');

ss= fspecial('gaussian',3);
ff = imfilter(cc,ss); 
subplot(1,2,2);
imshow(ff,[]),title('STEP:4 Using Gaussian Filter Smoothing Image:2');

figure();

%%% Image Segmentation Process:-

% STEP:5 CANNY EDGE DETECTION**********************************************

e=edge(f,'canny');
subplot(1,2,1);
imshow(e);
title('STEP:5 Edge Detection by Canny Filter Image:1');

ee=edge(ff,'canny');
subplot(1,2,2);
imshow(ee);
title('STEP:5 Edge Detection by Canny Filter Image:2');

figure();

%hough transform*******************************************************

%[XY,rect] = imcrop(e);
radii = 15:1:65;
h = circle_hough(e, radii, 'same', 'normalise');
peaks1 = circle_houghpeaks(h, radii, 'nhoodxy', 15, 'nhoodr', 21, 'npeaks', 2);
subplot(1,2,1);
imshow(f);
title('STEP:6 Hough Transform on Image:1');
hold on;
for peak = peaks1
   [x, y] = circlepoints(peak(3));
   plot(x+peak(1), y+peak(2), 'g-');
end
hold off

radii =20:1:65;
hh = circle_hough(ee, radii, 'same', 'normalise');
peaks2 = circle_houghpeaks(hh, radii, 'nhoodxy', 15, 'nhoodr', 21, 'npeaks', 2);
subplot(1,2,2);
imshow(ff);
title('STEP:6 Hough Transform on Image:2');
hold on;
for peak = peaks2
   [x, y] = circlepoints(peak(3));
   plot(x+peak(1), y+peak(2), 'g-');
end
hold off
figure();

%Normalization***********************************************************
xPosPupil = 93;
yPosPupil = 75;
rPupil = 23;
xPosIris = 94;
yPosIris = 75;
rIris = 56;
% Normalize the iris region according to daugmans model
irisRegion1 = rubberSheetNormalisation( f, xPosPupil, yPosPupil, rPupil , xPosIris , yPosIris , rIris, 'DebugMode', 1 );

xPosPupil2 = 73;
yPosPupil2= 78;
rPupil2 = 24;
xPosIris2 = 75;
yPosIris2 = 79;
rIris2 = 59;
% Normalize the iris region according to daugmans model
irisRegion2 = rubberSheetNormalisation( ff, xPosPupil2, yPosPupil2, rPupil2 , xPosIris2 , yPosIris2 , rIris2, 'DebugMode', 1 );

% Show Resulting image
subplot(1,2,1);
imshow(irisRegion1);
title('STEP:7 Normalization on Image:1');

subplot(1,2,2);
imshow(irisRegion2);
title('STEP:7 Normalization on Image:2');

%feature extraction******************************************************

gaborArray = gaborFilterBank(5,8,39,39);  % Generates the Gabor filter bank

featureVector1 = gaborFeatures(irisRegion1,gaborArray,4,4);   % Extracts Gabor feature vector, 'featureVector', from the image, 'img'.
%disp(featureVector);
featureVector2 = gaborFeatures(irisRegion2,gaborArray,4,4); 


%matching
d= sum(abs(featureVector1 - featureVector2)./(abs(featureVector1) + abs(featureVector2)));
disp(d);






%functions**********************************************************************

function [x, y] = circlepoints(r)
%CIRCLEPOINTS  Returns integer points close to a circle
%   [X, Y] = CIRCLEPOINTS(R) where R is a scalar returns coordinates of
%   integer points close to a circle of radius R, such that none is
%   repeated and there are no gaps in the circle (under 8-connectivity).
%
%   If R is a row vector, a circle is generated for each element of R and
%   the points concatenated.
%   Copyright David Young 2010
x = [];
y = [];
for rad = r
    [xp, yp] = circlepoints1(rad);
    x = [x xp];
    y = [y yp];
end
end
    
function [x, y] = circlepoints1(r)    
% Get number of rows needed to cover 1/8 of the circle
l = round(r/sqrt(2));
if round(sqrt(r.^2 - l.^2)) < l   % if crosses diagonal
    l = l-1;
end
% generate coords for 1/8 of the circle, a dot on each row
x0 = 0:l;
y0 = round(sqrt(r.^2 - x0.^2));
% Check for overlap
if y0(end) == l
    l2 = l;
else
    l2 = l+1;
end
% assemble first quadrant
x = [x0 y0(l2:-1:2)]; 
y = [y0 x0(l2:-1:2)];
% add next quadrant
x0 = [x y];
y0 = [y -x];
% assemble full circle
x = [x0 -x0];
y = [y0 -y0];
end

function [h, margin] = circle_hough(b, rrange, varargin)

opts = {'same' 'normalise'};
narginchk(2, 2+length(opts));
validateattributes(rrange, {'double'}, {'real' 'positive' 'vector'});
if ~all(ismember(varargin, opts))
    error('Unrecognised option');
end
% get indices of non-zero features of b
[featR, featC] = find(b);
% set up accumulator array - with a margin to avoid need for bounds checking
[nr, nc] = size(b);
nradii = length(rrange);
margin = ceil(max(rrange));
nrh = nr + 2*margin;        % increase size of accumulator
nch = nc + 2*margin;
h = zeros(nrh*nch*nradii, 1, 'uint32');  % 1-D for now, uint32 a touch faster
% get templates for circles at all radii - these specify accumulator
% elements to increment relative to a given feature
tempR = []; tempC = []; tempRad = [];
for i = 1:nradii
    [tR, tC] = circlepoints(rrange(i));
    tempR = [tempR tR]; %#ok<*AGROW>
    tempC = [tempC tC];
    tempRad = [tempRad repmat(i, 1, length(tR))];
end
% Convert offsets into linear indices into h - this is similar to sub2ind.
% Take care to avoid negative elements in either of these so can use
% uint32, which speeds up processing by a factor of more than 3 (in version
% 7.5.0.342)!
tempInd = uint32( tempR+margin + nrh*(tempC+margin) + nrh*nch*(tempRad-1) );
featInd = uint32( featR' + nrh*(featC-1)' );
% Loop over features
for f = featInd
    % shift template to be centred on this feature
    incI = tempInd + f;
    % and update the accumulator
    h(incI) = h(incI) + 1;
end
% Reshape h, convert to double, and apply options
h = reshape(double(h), nrh, nch, nradii);
if ismember('same', varargin)
    h = h(1+margin:end-margin, 1+margin:end-margin, :);
    margin = 0;
end
if ismember('normalise', varargin)
    h = bsxfun(@rdivide, h, reshape(rrange, 1, 1, length(rrange)));
end
end

function peaks = circle_houghpeaks(h, radii, varargin)
params = checkargs(h, radii, varargin{:});
% smooth the accumulator - xy
if params.smoothxy > 0
    [m, hsize] = gaussmask1d(params.smoothxy);
    % smooth each dimension separately, with reflection
    h = cat(1, h(hsize:-1:1,:,:), h, h(end:-1:end-hsize+1,:,:));
    h = convn(h, reshape(m, length(m), 1, 1), 'valid');
    
    h = cat(2, h(:,hsize:-1:1,:), h, h(:,end:-1:end-hsize+1,:));
    h = convn(h, reshape(m, 1, length(m), 1), 'valid');
end
% smooth the accumulator - r
if params.smoothr > 0
    [m, hsize] = gaussmask1d(params.smoothr);
    h = cat(3, h(:,:,hsize:-1:1), h, h(:,:,end:-1:end-hsize+1));
    h = convn(h, reshape(m, 1, 1, length(m)), 'valid');
end
% set threshold
if isempty(params.threshold)
    params.threshold = 0.5 * max(h(:));
end
if isempty(params.nhoodxy) && isempty(params.nhoodr)
    % First approach to peak finding: local maxima
    
    % find the maxima
    maxarr = imregionalmax(h);
    
    maxarr = maxarr & h >= params.threshold;
    
    % get array indices
    peakind = find(maxarr);
    [y, x, rind] = ind2sub(size(h), peakind);
    peaks = [x'; y'; radii(rind)];
    
    % get strongest peaks
    if ~isempty(params.npeaks) && params.npeaks < size(peaks,2)
        [~, ind] = sort(h(peakind), 'descend');
        ind = ind(1:params.npeaks);
        peaks = peaks(:, ind);
    end
    
else
    % Second approach: iterative global max with suppression
    if isempty(params.nhoodxy)
        params.nhoodxy = 1;
    elseif isempty(params.nhoodr)
        params.nhoodr = 1;
    end
    nhood2 = ([params.nhoodxy params.nhoodxy params.nhoodr]-1) / 2;
    
    if isempty(params.npeaks)
        maxpks = 0;
        peaks = zeros(3, round(numel(h)/100));  % preallocate
    else
        maxpks = params.npeaks;  
        peaks = zeros(3, maxpks);  % preallocate
    end
    
    np = 0;
    while true
        [r, c, k, v] = max3(h);
        % stop if peak height below threshold
        if v < params.threshold || v == 0
            break;
        end
        np = np + 1;
        peaks(:, np) = [c; r; radii(k)];
        % stop if done enough peaks
        if np == maxpks
            break;
        end
        % suppress this peak
        r0 = max([1 1 1], [r c k]-nhood2);
        r1 = min(size(h), [r c k]+nhood2);
        h(r0(1):r1(1), r0(2):r1(2), r0(3):r1(3)) = 0;
    end 
    peaks(:, np+1:end) = [];   % trim
end
% adjust for margin
if params.margin > 0
    peaks([1 2], :) = peaks([1 2], :) - params.margin;
end
end
function params = checkargs(h, radii, varargin)
% Argument checking
ip = inputParser;
% required
htest = @(h) validateattributes(h, {'double'}, {'real' 'nonnegative' 'nonsparse'});
ip.addRequired('h', htest);
rtest = @(radii) validateattributes(radii, {'double'}, {'real' 'positive' 'vector'});
ip.addRequired('radii', rtest);
% optional
mtest = @(n) validateattributes(n, {'double'}, {'real' 'nonnegative' 'integer' 'scalar'});
ip.addOptional('margin', 0, mtest); 
% parameter/value pairs
stest = @(s) validateattributes(s, {'double'}, {'real' 'nonnegative' 'scalar'});
ip.addParameter('smoothxy', 0, stest);
ip.addParameter('smoothr', 0, stest);
ip.addParameter('threshold', [], stest);
nptest = @(n) validateattributes(n, {'double'}, {'real' 'positive' 'integer' 'scalar'});
ip.addParameter('npeaks', [], nptest);
nhtest = @(n) validateattributes(n, {'double'}, {'odd' 'positive' 'scalar'});
ip.addParameter('nhoodxy', [], nhtest);
ip.addParameter('nhoodr', [], nhtest);
ip.parse(h, radii, varargin{:});
params = ip.Results;
end
function [m, hsize] = gaussmask1d(sigma)
% truncated 1D Gaussian mask
hsize = ceil(2.5*sigma);  % reasonable truncation
x = (-hsize:hsize) / (sqrt(2) * sigma);
m = exp(-x.^2);
m = m / sum(m);  % normalise
end
function [r, c, k, v] = max3(h)
% location and value of global maximum of a 3D array
[vr, r] = max(h);
[vc, c] = max(vr);
[v, k] = max(vc);
c = c(1, 1, k);
r = r(1, c, k);
end

%Normalization*************************************************************

function image = rubberSheetNormalisation( img, xPosPupil, yPosPupil, rPupil , xPosIris , yPosIris , rIris , varargin )

    %todo: remove for-loop for line detection
    if(size(img, 3) == 3) % if RGB image is inputted
       img = rgb2gray(img);
    end
    
    % parse input
    p = inputParser();
    addRequired( p , 'xPosPupil' , @isnumeric );
    addRequired( p , 'yPosPupil' , @isnumeric );
    addRequired( p , 'rPupil' , @isnumeric );
    addRequired( p , 'xPosIris' , @isnumeric );
    addRequired( p , 'yPosIris' , @isnumeric );
    addRequired( p , 'rIris' , @isnumeric );
    addOptional( p , 'AngleSamples', 360 ,@isnumeric );
    addOptional( p , 'RadiusSamples', 360 ,@isnumeric );
    addOptional( p , 'DebugMode', 0, @isnumeric );
    addOptional( p , 'UseInterpolation', 1, @isnumeric );
    parse( p , xPosPupil, yPosPupil, rPupil , xPosIris , yPosIris , rIris , varargin{:} )
    
    % Note that internally matrix coordinates are used
    xp = p.Results.yPosPupil;
    yp = p.Results.xPosPupil; 
    rp = p.Results.rPupil;
    xi = p.Results.yPosIris;
    yi = p.Results.xPosIris;
    ri = p.Results.rIris;
    angleSamples = p.Results.AngleSamples;
    RadiusSamples = p.Results.RadiusSamples;
    debug = p.Results.DebugMode;
    interpolateQ = p.Results.UseInterpolation;
    
    % Initialize samples 
    angles = (0:pi/angleSamples:pi-pi/angleSamples) + pi/(2*angleSamples);%avoiding infinite slope
    r = 0:1/RadiusSamples:1;
    nAngles = length(angles);
    
    % Calculate pupil points and iris points that are on the same line
    x1 = ones(size(angles))*xi;
    y1 = ones(size(angles))*yi;
    x2 = xi + 10*sin(angles);
    y2 = yi + 10*cos(angles);
    dx = x2 - x1;
    dy = y2 - y1;
    slope = dy./dx;
    intercept = yi - xi .* slope;
    
    xout = zeros(nAngles,2);
    yout = zeros(nAngles,2);
    for i = 1:nAngles
        [xout(i,:),yout(i,:)] = linecirc(slope(i),intercept(i),xp,yp,rp);
    end
       
    % Get samples on limbus boundary
    xRightIris = yi + ri * cos(angles);
    yRightIris = xi + ri * sin(angles);
    xLeftIris = yi - ri * cos(angles);
    yLeftIris = xi - ri * sin(angles);
    
    
    % Get samples in radius direction
    xrt = (1-r)' * xout(:,1)' + r' * yRightIris;
    yrt = (1-r)' * yout(:,1)' + r' * xRightIris;
    xlt = (1-r)' * xout(:,2)' + r' * yLeftIris;
    ylt = (1-r)' * yout(:,2)' + r' * xLeftIris;
    
    % Create Normalized Iris Image
    if interpolateQ
        image = uint8(reshape(interp2(double(img),[yrt(:);ylt(:)],[xrt(:);xlt(:)]),length(r), 2*length(angles))');
    else
        image = reshape(img(sub2ind(size(img),round([xrt(:);xlt(:)]),round([yrt(:);ylt(:)]))),length(r), 2*length(angles));
    end
       
    % Show all points on original input image
    if debug
        
        img = insertShape(img, 'circle', [yrt(:),xrt(:),2*ones(size(xrt(:)))],'Color','r');
        img = insertShape(img, 'circle', [ylt(:),xlt(:),2*ones(size(xrt(:)))],'Color','r');
        
        figure('name','Sample scheme of the rubber sheet normalization');
        imshow(img);
        drawnow;
        
    end
    
end

%FE************************************************
function gaborArray = gaborFilterBank(u,v,m,n)

if (nargin ~= 4)    % Check correct number of arguments
    error('There must be four input arguments (Number of scales and orientations and the 2-D size of the filter)!')
end
%Create Gabor filters
% Create u*v gabor filters each being an m by n matrix
gaborArray = cell(u,v);
fmax = 0.25;
gama = sqrt(2);
eta = sqrt(2);
for i = 1:u
    
    fu = fmax/((sqrt(2))^(i-1));
    alpha = fu/gama;
    beta = fu/eta;
    
    for j = 1:v
        tetav = ((j-1)/v)*pi;
        gFilter = zeros(m,n);
        
        for x = 1:m
            for y = 1:n
                xprime = (x-((m+1)/2))*cos(tetav)+(y-((n+1)/2))*sin(tetav);
                yprime = -(x-((m+1)/2))*sin(tetav)+(y-((n+1)/2))*cos(tetav);
                gFilter(x,y) = (fu^2/(pi*gama*eta))*exp(-((alpha^2)*(xprime^2)+(beta^2)*(yprime^2)))*exp(1i*2*pi*fu*xprime);
            end
        end
        gaborArray{i,j} = gFilter;
        
    end
end
% %% Show Gabor filters (Please comment this section if not needed!)
% % Show magnitudes of Gabor filters:
% figure('NumberTitle','Off','Name','Magnitudes of Gabor filters');
% for i = 1:u
%     for j = 1:v        
%         subplot(u,v,(i-1)*v+j);        
%         imshow(abs(gaborArray{i,j}),[]);
%     end
% end
% % Show real parts of Gabor filters:
% figure('NumberTitle','Off','Name','Real parts of Gabor filters');
% for i = 1:u
%     for j = 1:v        
%         subplot(u,v,(i-1)*v+j);        
%         imshow(real(gaborArray{i,j}),[]);
%     end
% end
end

function featureVector = gaborFeatures(img,gaborArray,d1,d2)

if (nargin ~= 4)        % Check correct number of arguments
    error('Please use the correct number of input arguments!')
end
if size(img,3) == 3     % Check if the input image is grayscale
    warning('The input RGB image is converted to grayscale!')
    img = rgb2gray(img);
end
img = double(img);
%Filter the image using the Gabor filter bank
% Filter input image by each Gabor filter
[u,v] = size(gaborArray);
gaborResult = cell(u,v);
for i = 1:u
    for j = 1:v
        gaborResult{i,j} = imfilter(img, gaborArray{i,j});
    end
end
%Create feature vector
% Extract feature vector from input image
featureVector = [];
for i = 1:u
    for j = 1:v
        
        gaborAbs = abs(gaborResult{i,j});
        gaborAbs = downsample(gaborAbs,d1);
        gaborAbs = downsample(gaborAbs.',d2);
        gaborAbs = gaborAbs(:);
        
        % Normalized to zero mean and unit variance. (if not applicable, please comment this line)
        gaborAbs = (gaborAbs-mean(gaborAbs))/std(gaborAbs,1);
        
        featureVector =  [featureVector; gaborAbs];
        
    end
end
%% Show filtered images (Please comment this section if not needed!)
% % Show real parts of Gabor-filtered images
% figure('NumberTitle','Off','Name','Real parts of Gabor filters');
% for i = 1:u
%     for j = 1:v        
%         subplot(u,v,(i-1)*v+j)    
%         imshow(real(gaborResult{i,j}),[]);
%     end
% end
% 
% % Show magnitudes of Gabor-filtered images
% figure('NumberTitle','Off','Name','Magnitudes of Gabor filters');
% for i = 1:u
%     for j = 1:v        
%         subplot(u,v,(i-1)*v+j)    
%         imshow(abs(gaborResult{i,j}),[]);
%     end
% end
end