% segmentiris - peforms automatic segmentation of the iris region
% from an eye image. Also isolates noise areas such as occluding
% eyelids and eyelashes.
%
% Usage: 
% [circleiris, circlepupil, imagewithnoise] = segmentiris(image)
%
% Arguments:
%	eyeimage		- the input eye image
%	
% Output:
%	circleiris	    - centre coordinates and radius
%			          of the detected iris boundary
%	circlepupil	    - centre coordinates and radius
%			          of the detected pupil boundary
%	imagewithnoise	- original eye image, but with
%			          location of noise marked with
%			          NaN values
%
eyeimage=imread('D:/College/BE project/project/eyecroppp.bmp');
[circleiris, circlepupil, imagewithnoise] = segmentiris(eyeimage);
function [circleiris, circlepupil, imagewithnoise] = segmentiris(eyeimage)

% define range of pupil & iris radii

%CASIA
lpupilradius = 28;
upupilradius = 75;
lirisradius = 80;
uirisradius = 150;

% As For the CASIA database, values of the iris radius range from 90 to 150 pixels,
% while the pupil radius ranges from 28 to 75 pixels.

%    %LIONS
%    lpupilradius = 32;
%    upupilradius = 85;
%    lirisradius = 145;
%    uirisradius = 169;


% define scaling factor to speed up Hough transform
scaling = 0.4;

reflecthres = 240;

% find the iris boundary using Hough Transform and Canny edge detection
[row, col, r] = findcircle(eyeimage, lirisradius, uirisradius, scaling, 2, 0.20, 0.19, 1.00, 0.00);

circleiris = [row col r];

rowd = double(row);
cold = double(col);
rd = double(r);

irl = round(rowd-rd);
iru = round(rowd+rd);
icl = round(cold-rd);
icu = round(cold+rd);

imgsize = size(eyeimage);

if irl < 1 
    irl = 1;
end

if icl < 1
    icl = 1;
end

if iru > imgsize(1)
    iru = imgsize(1);
end

if icu > imgsize(2)
    icu = imgsize(2);
end

% to find the inner pupil, use just the region within the previously detected iris boundary
imagepupil = eyeimage( irl:iru,icl:icu);

%find pupil boundary
[rowp, colp, r] = findcircle(imagepupil, lpupilradius, upupilradius ,0.6,2,0.25,0.25,1.00,1.00);

rowp = double(rowp);
colp = double(colp);
r = double(r);

row = double(irl) + rowp;
col = double(icl) + colp;

row = round(row);
col = round(col);

circlepupil = [row col r];

% set up array for recording noise regions noise pixels will have NaN values
imagewithnoise = double(eyeimage);

%find top eyelid
topeyelid = imagepupil(1:(rowp-r),:);
lines = findline(topeyelid);

if size(lines,1) > 0
    [xl, yl] = linecoords(lines, size(topeyelid));
    yl = double(yl) + irl-1;
    xl = double(xl) + icl-1;
    
    yla = max(yl);
    
    y2 = 1:yla;
    
    ind3 = sub2ind(size(eyeimage),yl,xl);
    imagewithnoise(ind3) = NaN;
    
    imagewithnoise(y2, xl) = NaN;
end

%find bottom eyelid
bottomeyelid = imagepupil((rowp+r):size(imagepupil,1),:);
lines = findline(bottomeyelid);

if size(lines,1) > 0
    
    [xl, yl] = linecoords(lines, size(bottomeyelid));
    yl = double(yl)+ irl+rowp+r-2;
    xl = double(xl) + icl-1;
    
    yla = min(yl);
    
    y2 = yla:size(eyeimage,1);
    
    ind4 = sub2ind(size(eyeimage),yl,xl);
    imagewithnoise(ind4) = NaN;
    imagewithnoise(y2, xl) = NaN;
    
end

%For CASIA, eliminate eyelashes by thresholding
ref = eyeimage < 100;
coords = ref==1;
imagewithnoise(coords) = NaN;
end

% findcircle - returns the coordinates of a circle in an image using the Hough transform
% and Canny edge detection to create the edge map.
%
% Usage: 
% [row, col, r] = findcircle(image,lradius,uradius,scaling, sigma, hithres, lowthres, vert, horz)
%
% Arguments:
%	image		    - the image in which to find circles
%	lradius		    - lower radius to search for
%	uradius		    - upper radius to search for
%	scaling		    - scaling factor for speeding up the Hough transform
%	sigma		    - amount of Gaussian smoothing to apply for creating edge map.
%	hithres		    - threshold for creating edge map
%	lowthres	    - threshold for connected edges
%	vert		    - vertical edge contribution (0-1)
%	horz		    - horizontal edge contribution (0-1)
%	
% Output:
%	circleiris	    - centre coordinates and radius of the detected iris boundary
%	circlepupil	    - centre coordinates and radius of the detected pupil boundary
%	imagewithnoise	- original eye image, but with location of noise marked with
%			          NaN values
%

function [row, col, r] = findcircle(image,lradius,uradius,scaling, sigma, hithres, lowthres, vert, horz)

lradsc = round(lradius*scaling);
uradsc = round(uradius*scaling);
rd = round(uradius*scaling - lradius*scaling);

% generate the edge image
[I2, or] = canny(image, sigma, scaling, vert, horz);     % canny function for edgemap
I3 = adjgamma(I2, 1.9);                                 % to adjust gamma portion i.e to enhance the contrast
I4 = nonmaxsup(I3, or, 1.5);                            % for performing non-maxima suppression on an image using an orientation image, 
%figure, imshow(I4);title('aa');

edgeimage = hysthresh(I4, hithres, lowthres);           % For edge marking
%figure,imshow(edgeimage);

% perform the circular Hough transform
h = houghcircle(edgeimage, lradsc, uradsc);

maxtotal = 0;

% find the maximum in the Hough space, and hence the parameters of the circle
for i=1:rd
    
    layer = h(:,:,i);
    [maxlayer] = max(max(layer));
    
    
    if maxlayer > maxtotal
        
        maxtotal = maxlayer;
        
        
        r = int32((lradsc+i) / scaling);
        
        [row,col] = ( find(layer == maxlayer) );
        
        
        row = int32(row(1) / scaling); % returns only first max value
        col = int32(col(1) / scaling);    
        
    end
    
    
end
end